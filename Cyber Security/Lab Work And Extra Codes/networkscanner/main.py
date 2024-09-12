
# manually we can check all live ips using netdiscover
# netdiscover -r 192.168.21.1/24
# program to send arp broadcast request of gateway ip route -n to know mac of same and all in network

import scapy.all as scapy

def scan(ip):
    scapy.arping(ip)

#scan("192.168.254.2")
scan("192.168.254.2/24")
