#layer which contains uname and pass is a RAW layer

import scapy.all as scapy
from scapy.layers import http

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        if packet.haslayer(scapy.Raw): #write any layer for which you are looking for here
           print(packet[scapy.Raw].load) #it will omit all other layer display only raw display with load field

sniff("eth0")