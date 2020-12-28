# encoding:utf-8
import bitnodes_extract
import fdns_extract
import ripe_atlas_extract
import ripe_ipmap_extract
import TLDR_extract
import datetime
import time

def core_collect():
    date=str(datetime.datetime.now()).split()[0]
    print(str(date)+" begin collect")
    print("collect IPv6 from bitnodes")
    bitnodes_extract.getALLsnapshots()
    print("collect IPv6 from fdns")
    fdns_extract.download()
    print("collect IPv6 from atlas")
    ripe_atlas_extract.download()
    print("collect IPv6 from ipmap")
    ripe_ipmap_extract.download()
    print("collect IPv6 from TLDR")
    TLDR_extract.download()
    date=datetime.datetime.now()
    print("[+]"+str(date)+"runing over")
      
def running():
    core_collect()
     

if __name__ == "__main__":
    running()

