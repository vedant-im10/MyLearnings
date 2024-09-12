
import subprocess
import optparse

def change_mac(interface, new_mac):
    print("[+] changing MAC address for " + interface + " to " + new_mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface", help="interface to change its mac address")
parser.add_option("-m", "--mac", dest="new_mac", help="new mac address")

(options, arguments) = parser.parse_args()

change_mac(options.interface, options.new_mac)