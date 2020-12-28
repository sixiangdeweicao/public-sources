# encoding:utf-8

import requests
from bs4 import BeautifulSoup
import re
import os
import subprocess
from utils import shell
import datetime


def download(save_dir = "/data/tmp/",final_save_dir = "/data/sources/fdns/"):
    url = "https://opendata.rapid7.com/sonar.fdns_v2/"  # nice
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    tag = soup.select("div[class='table-scroll']")[0]  # 有二个0,1，第二个需要注册账户即可免费获取
    for a_tag in tag.select("a"):
        if a_tag.has_attr('href') and "aaaa" in a_tag.attrs['href']:
            relative_url = a_tag.attrs['href']
            # print(relative_url)  # /sonar.fdns_v2/2019-05-24-1558737480-fdns_aaaa.json.gz
            break

    root = "https://opendata.rapid7.com"
    date = re.search(r"/[\d]*-[\d]*-[\d]*", relative_url)
    date = date.group().strip("/")
    gz_name = relative_url.rsplit("/", 1)[1]
    name = gz_name.rsplit(".", 1)[0]
    date = name.rsplit("-", 2)[0]

    os.chdir(save_dir)
    if not os.path.exists(name) and not os.path.exists(gz_name):
        # input(">This py need much time, go?")
        os.popen("wget " + root + relative_url).read()
    while True:
        if not os.path.exists(name):
            # input(">This py need much time, again. Go?")
            if "not found" in shell("gzip -d " + name):
                print("[-]Install gzip first")
                exit()
        else:
            break
    # 解压后有 67 G
    print("[+]Handle ..... ")
    IPv6_addr = []
    for line in open(name):
        if re.search('"type":"aaaa"', line) != None:
            for ipv6 in re.findall(r'\"value\":\"([0-9|a-f|:]*)\"', line):
                if ":" in ipv6:
                    IPv6_addr.append(ipv6)

    print("[+]", len(IPv6_addr))
    date=str(datetime.datetime.now()).split()[0]
    with open(final_save_dir + date + ".fdns", "w") as f:
        for ipv6 in IPv6_addr:
            f.write(ipv6 + "\n")
    print("[+Save ", final_save_dir + date + ".fdns")
    os.remove(name)

# 考虑到文件太大就不删除了
# download()


