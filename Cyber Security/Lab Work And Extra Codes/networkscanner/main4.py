# program of setting destination mac to bradcast mac so that arp request packet can be send to all
# create ethernet frame to send bradcast mac address


import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip) #arp_request is having instance of ARP packet object made by scapy
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") #ethernet object created from scapy with instance in broadcast
    #scapy.ls(scapy.Ether())
    print(broadcast.summary())




#scan("192.168.254.2")
scan("192.168.254.2/24")