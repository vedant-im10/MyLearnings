#sniff user name and password on http login page not on https
#run testphp vulnweb

import scapy.all as scapy
from scapy.layers import http


def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)
    #scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet, filter = "port 21")
    #filter can be used for any other except http

def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        print(packet)

sniff("eth0")