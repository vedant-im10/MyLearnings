#use regular expression to ignore everything and read only mac address
#copy ifconfig result from terminal and put it inside pythex to test different command from cheatsheet
# . , \d , <.*> , \w ,\w\w:\w\w:\w\w:\w\w:\w\w:\w\w



import subprocess
import optparse
import re


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
change_mac(options.interface, options.new_mac)
ifconfig_result = subprocess.check_output(["ifconfig", options.interface])
print(ifconfig_result)
# from which text you want to search
mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

if mac_address_search_result:
    print(mac_address_search_result.group(0))
    # group 0 will only extract first occurance result from group of similar results of mac address
else:
    print("[-] could not read mac address") # for reading interface error for "lo"
