

import subprocess


subprocess.call("ifconfig eth0 down", shell=True)
subprocess.call("ifconfig eth0 hw ether 00:22:44:55:66:88",  shell=True)
subprocess.call("ifconfig eth0 up", shell=True)