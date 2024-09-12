
# final step for parse the responses
import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1)[0]
    #it will only return me answered list by writing index [0]
    for element in answered_list:
        print(element[1].psrc)  #ip of client packet
        print(element[1].hwsrc)  #mac of client packet

        print("-------------------------------------------------------------------------------------")

#scan("192.168.254.2")
scan("192.168.254.2/24")