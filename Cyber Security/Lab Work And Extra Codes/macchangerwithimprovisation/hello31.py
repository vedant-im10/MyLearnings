
#to display help message using python3 hello31.py --help
#to get idea about which kind of cli argument we can write

import subprocess
import optparse  # allows to get user argument and parse it to the code
parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface", help="interface to change its mac address")
parser.parse_args()

interface = input("interface >  ")
new_mac = input("new MAC > ")

print("[+] changing MAC address for " + interface + " to  new_mac")


subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)