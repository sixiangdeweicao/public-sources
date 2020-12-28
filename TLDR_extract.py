# encoding:utf-8
import os
import subprocess
from utils import shell
import gzip
import datetime
import shutil

def download(save_dir= "/data/tmp/",final_save_dir = "/data/sources/TLDR/"):
    os.chdir(save_dir)
    if not os.path.exists("TLDR"):
        if "not found" in shell("git clone https://github.com/mandatoryprogrammer/TLDR.git"):
            print("[-}Install git first")
            exit()
    else:
        print("[+]TLDR exists")
    # print("begin")
    # print(os.getcwd())
    valid = []
    IPv6_addr = [] 
    for root, dirs, files in os.walk(os.getcwd() + os.sep + "TLDR/archives/"):
        for name in files:   
            if name.find(".gz")>0:
                continue              
            for line in open(root + os.sep + name,"r"):
                if line[0] != ";" and line.strip() != "":
                    valid.append(line)
                    if "AAAA" in line:
                        IPv6_addr.append(line.strip().split()[-1:][0])
                    # print line
                    # print root + os.sep + name

    # with open("./valid.TLDR","w") as f:
    #     f.writelines(valid)
    print("[+]find ipv6 {}".format(len(IPv6_addr)))
    date=str(datetime.datetime.now()).split()[0]
    with open(final_save_dir + date + ".tldr", "w") as f:
        for ipv6 in IPv6_addr:
            f.write(ipv6 + "\n")
    print("[+]Save ", final_save_dir + date + ".tldr")

    if os.path.exists("./valid.TLDR"):
        os.remove("valid.TLDR")

    shutil.rmtree(save_dir + "TLDR")

# download()