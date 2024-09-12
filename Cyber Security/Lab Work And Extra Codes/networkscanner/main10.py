

# concept of dictionary
import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    #it will only return me answered list by writing index [0]

    print("IP \t\t\t\t MAC Address\n--------------------------------------------------")
    clients_list = []

    for element in answered_list:
        clients_dict = {"ip": element[1].psrc, "Mac": element[1].hwsrc}
        clients_list.append(clients_dict)
        print(element[1].psrc + "\t\t\t" + element[1].hwsrc)
    print(clients_list)

#scan("192.168.254.2")
scan("192.168.254.2/24")