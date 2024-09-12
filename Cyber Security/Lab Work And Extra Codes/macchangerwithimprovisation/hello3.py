#handling cli argument directly
#run with python hello3.py --interface eth0 --mac 00:11...


import subprocess
import optparse  # allows to get user argument and parse it to the code
parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface", help="interface to change its mac address")
parser.add_option("-m", "--mac", dest="new_mac", help="new mac address")


(options, arguments) = parser.parse_args() # will return two sets of information

interface = options.interface
new_mac = options.new_mac

#  print("[+] changing MAC address for " + interface + " to " + new_mac)


subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])
