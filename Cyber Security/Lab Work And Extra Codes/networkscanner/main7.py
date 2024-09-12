
#parsing response which we got in previous step in list
#we want only mac address and ip from response packet
import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1)[0]
    #it will only return me answered list by writing index [0]
    for element in answered_list:
        #print(element[1])  #  only fetch answer not packet sent, raw packet display
        print(element[1].show())
        print("-------------------------------------------------------------------------------------")

#scan("192.168.254.2")
scan("192.168.254.2/24")