# encoding:utf-8

import requests
from bs4 import BeautifulSoup
import os
import subprocess
import re
from utils import shell
import datetime

def getLatest(url, pattern):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    latest = ""
    for a_tag in soup.select("a"):
        dir = a_tag.attrs['href']
        if re.match(pattern, dir) != None:
            latest = dir
        else:
            if latest != "":
                break
    url += latest
    return url

def download(save_dir = "/data/tmp/",final_save_dir = "/data/sources/ripe_atlas/"):
    url = "https://ftp.ripe.net/ripe/atlas/probes/archive/"
    # 找到最新年份
    url = getLatest(url, "[\d]+/")

    # 找到最新月份
    url = getLatest(url, "[\d]+/")

    # 找到最新日期文件
    url = getLatest(url, "[\d]+.json.bz2")

    os.chdir(save_dir)
    bz2_name = url.rsplit("/", 1)[1]
    name = bz2_name.rsplit(".", 1)[0]
    date = name.split(".")[0]
    if not os.path.exists(bz2_name):
        shell("wget " + url)
    if not os.path.exists(name):
        if "not found" in shell("bzip2 -d " + bz2_name):
            print("[-]install bzip2 first")
            exit()

    name=save_dir+name
    with open(name) as f:
        content = f.read()
    IPv6_addr = re.findall(r'\"address_v6\":\"([0-9|a-f|:]*)\"', content)
    print("[+]", len(IPv6_addr))
    date=str(datetime.datetime.now()).split()[0]
    with open(final_save_dir + date + ".ripe_atlas", "w") as f:
        for ipv6 in IPv6_addr:
            f.write(ipv6 + "\n")
   
    print("[+]Save ", final_save_dir + date + ".ripe_atlas")
    os.remove(name)

# download()

