#program to send first step packet and receive response from all host in a network

import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip) #arp_request is having instance of ARP packet object made by scapy
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") #ethernet object created from scapy with instance in broadcast
    arp_request_broadcast = broadcast/arp_request #combine first two to have one complete packet of step 1
    answered, unanswered = scapy.srp(arp_request_broadcast, timeout=1)  #this will send packet to all and catch couple of response
    #srp--> send and receive packet with cutome ether part which we used in broadcast
    #doc of srp
    #timeout will wait for 1 second to capture answered and unanswered responses then timeout
    print(answered.summary())
    #print(unanswered.summary())


#scan("192.168.254.2")
scan("192.168.254.2/24")