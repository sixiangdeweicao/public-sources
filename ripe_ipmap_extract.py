# encoding:utf-8

import requests
from bs4 import BeautifulSoup
import os
import subprocess
from utils import shell
import datetime

url = "https://ftp.ripe.net/ripe/ipmap/"


def extractPage():
    r = requests.get(url)
    soup = BeautifulSoup(r.text,"html.parser")
    latest_geolactions_file = soup.select("a")[-1:][0].attrs['href']
    return latest_geolactions_file


def download(save_dir = "/data/tmp/",final_save_dir = "/data/sources/ripe_ipmaps/"):
    filename = extractPage()
    if not os.path.exists(save_dir + filename):
        r = requests.get(url + filename)
        with open(save_dir + filename, 'wb') as f:
            f.write(r.content)
    new_filename = filename.rsplit(".", 1)[0]
    if not os.path.exists(save_dir + new_filename):
        if "not" in shell("bzip2 -d " + save_dir + filename):
            print("[-]Install bzip2 first")
            os.remove(save_dir + filename)
            exit()
    # print("[+] %s" % new_filename)
    with open(save_dir + new_filename) as f:
        lines = f.readlines()
    IPv6_addr = []
    for line in lines:
        addr = line.split(",")[0]
        if ":" in addr:
            IPv6_addr.append(addr)
    # print(len(lines))
    print("[+]Total ipv6 addr:" + str(len(IPv6_addr)))
    date=str(datetime.datetime.now()).split()[0]
    with open(final_save_dir + date + ".ripe_ipmap", "w") as f:
        for ipv6 in IPv6_addr:
            f.write(ipv6 + "\n")
    date=str(datetime.datetime.now()).split()[0]
    print("[+]Save ", final_save_dir + date + ".ripe_ipmap")
    os.remove(save_dir + new_filename)


# download()





