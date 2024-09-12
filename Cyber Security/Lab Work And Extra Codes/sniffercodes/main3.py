#instead of displaying all i want to display only user name and password
#check packet.show to see which layer and which field is used for sending uname and pass
#configure terminal fro infinite scrolling instead of 500 lines as it will show many info
#show will give response layer wise
#uname and password are sent using HTTP POST method so chk for post and you will get unmae and password
#see for post request in http

import scapy.all as scapy
from scapy.layers import http

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
       #                                                                                                                                                                                                                                                                                                                                 print(packet.show())
        url = packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path
        print(url)
        #print(packet.show())

sniff("eth0")