# encoding:utf-8

import requests
import json
import time
import datetime

def getLatest(final_save_dir = "/data/sources/bitnodes/"):
    date = ""
    url = "https://bitnodes.earn.com/api/v1/snapshots/latest/"  # 读取最新快照，手册：https://bitnodes.earn.com/api/
    headers = {
        "Accept": "application/json"
    }
    r = requests.get(url, headers=headers)
    IPv6_addr = []
    for k, v in json.loads(r.text.encode("utf-8"))['nodes'].items():
        if ":" in k and "[" in k:
            ipv6 = k.rsplit(":", 1)[0].strip("[]")
            # print(ipv6)
            IPv6_addr.append(ipv6)

    time_stamp = json.loads(r.text.encode("utf-8"))['timestamp']
    timeArray = time.localtime(time_stamp)
    date = time.strftime("%Y-%m-%d", timeArray)
    # print("[+]" + date)
    # print("[+]", len(IPv6_addr))
    with open(final_save_dir + date + ".bitnodes", "w") as f:
        for ipv6 in IPv6_addr:
            f.write(ipv6 + "\n")

def getALLsnapshots(final_save_dir = "/data/sources/bitnodes/"):

    snapshots_api = "https://bitnodes.earn.com/api/v1/snapshots/"
    url = "https://bitnodes.earn.com/api/v1/snapshots/"
    headers = {
        "Accept": "application/json"
    }
    r = requests.get(snapshots_api, headers=headers)
    IPv6_addr = []
    date = ""
    for snapshot in json.loads(r.text.encode("utf-8"))["results"]:
        time_stamp = snapshot['timestamp']
        if date == "":
            date = time_stamp
        r2 = requests.get(url + str(time_stamp) + "/", headers=headers)
        for k, v in json.loads(r2.text.encode("utf-8"))['nodes'].items():
            if ":" in k and "[" in k:
                ipv6 = k.rsplit(":", 1)[0].strip("[]")
                # print(ipv6)
                IPv6_addr.append(ipv6)
        # print("[+]Finish %d" % time_stamp)

    timeArray = time.localtime(date)
    date = time.strftime("%Y-%m-%d", timeArray)
    # print("[+]" + date)
    print("[+]Total:", len(IPv6_addr))
    IPv6_addr = list(set(IPv6_addr))
    print("[+]Duplicate removal:", len(IPv6_addr))
    date=str(datetime.datetime.now()).split()[0]
    with open(final_save_dir + date + ".bitnodes", "w") as f:
        for ipv6 in IPv6_addr:
            f.write(ipv6 + "\n")
    date=str(datetime.datetime.now()).split()[0]
    print("[+]Save ", final_save_dir + date + ".bitnodes")

# getALLsnapshots()


