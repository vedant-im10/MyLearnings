# program of combine first two substeps



import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip) #arp_request is having instance of ARP packet object made by scapy
    arp_request.show()
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") #ethernet object created from scapy with instance in broadcast
    broadcast.show()
    #scapy.ls(scapy.Ether())
    #print(broadcast.summary())
    arp_request_broadcast = broadcast/arp_request #combine first two to have one complete packet of step 1
    print(arp_request_broadcast.summary())
    arp_request_broadcast.show() # to know more details about this packet



#scan("192.168.254.2")
scan("192.168.254.2/24")