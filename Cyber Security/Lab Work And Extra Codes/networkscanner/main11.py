
#make print function for more improvisation in dictionary
#two different functions for scan and print
import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    #it will only return me answered list by writing index [0]

    clients_list = [] # creation of list of dictionary

    for element in answered_list:
        clients_dict = {"ip": element[1].psrc, "Mac": element[1].hwsrc}
        clients_list.append(clients_dict)
    return clients_list

def print_result(results_list):
    print("IP \t\t\t\t MAC Address\n--------------------------------------------------")
    for client in results_list:
        print(client)


#scan("192.168.254.2")
scan_result = scan("192.168.254.2/24")
print_result(scan_result)