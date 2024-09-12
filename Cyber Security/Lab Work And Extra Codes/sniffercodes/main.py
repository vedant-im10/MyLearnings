#specify interface on to which you want to sniff packet
#store argument is false we dont want to store packets on to system
#prn is callback fuction which is called when packet is captured on eth0
#response will jibrish which is not interpretable

import scapy.all as scapy


def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)


def process_sniffed_packet(packet):
    print(packet)


sniff("eth0")
