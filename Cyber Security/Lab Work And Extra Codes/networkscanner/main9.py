
# improve result printing like netdiscover with tables in output
#like netdiscover -r 192.168.254.2/24
# we dont want srp to display more info like finished,send...etc
# set srp in less verbose mode
import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    #it will only return me answered list by writing index [0]

    print("IP \t\t\t\t MAC Address\n--------------------------------------------------")
    for element in answered_list:
        print(element[1].psrc + "\t\t\t" + element[1].hwsrc)

#scan("192.168.254.2")
scan("192.168.254.2/24")