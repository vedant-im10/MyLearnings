# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 14:34:30 2021

@author: vedpa
"""

import socket
import sys
 
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print ("Socket successfully created")
except socket.error as err:
    print ("socket creation failed with error %s" %(err))
 
port = 80
 
try:
    host_ip = socket.gethostbyname('www.google.com')
except socket.gaierror:
    print ("there was an error resolving the host")
    sys.exit()

s.connect((host_ip, port))
 
print ("The socket has successfully connected to google.")