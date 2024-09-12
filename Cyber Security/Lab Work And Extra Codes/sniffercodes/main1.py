#to extract data which is useful and interpretable perform filtering
#add filter argument in sniff
#but filter does not filter traffic on port 80 or to and from web site
#install third party module called as scapy_http
#open any web site while running like bing.com to see http request,,local traffic from own browser

import scapy.all as scapy
from scapy.layers import http


def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)


def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest): #layer which we are requesting has http request or not using haslayer method of scapy
        #video, image all send using web browser are always sent using http layer
        print(packet)


sniff("eth0")