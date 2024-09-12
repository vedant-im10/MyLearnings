# system command execution with check of what ifconfig returns
# reading the output of system command
# using subprocess.chk_output doc display
#display same result as ifconfig eth0
#run with python main.py -i eth0 -m 00:....

import subprocess
import optparse


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="interface to change its mac address")
    parser.add_option("-m", "--mac", dest="new_mac", help="new mac address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("please specify an interface , use --help for more information")
    elif not options.new_mac:
        parser.error("please specify a new mac , use --help for more information")
    return options


def change_mac(interface, new_mac):
    print("[+] changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


options = get_arguments()
change_mac(options.interface, options.new_mac) #can be commented
ifconfig_result = subprocess.check_output(["ifconfig", options.interface]) #like ifconfig eth0
print(ifconfig_result)
