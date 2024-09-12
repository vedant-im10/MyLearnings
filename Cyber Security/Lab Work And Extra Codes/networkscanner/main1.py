# program without using arping

import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP() #arp_request is having instance of ARP packet object made by scapy
    print(arp_request.summary()) #generate arp request with 0.0.0.0

#scan("192.168.254.2")
scan("192.168.254.2/24")