


import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP() #arp_request is having instance of ARP packet object made by scapy
    arp_request.pdst = ip #passing ip to check ipfield change to router ip from 0.0.0.0
    print(arp_request.summary()) #generate arp request with 0.0.0.0
    scapy.ls(scapy.ARP())  #to know which field we can set to use ipfield instead of 0.0.0.0

#scan("192.168.254.2")
scan("192.168.254.2/24")