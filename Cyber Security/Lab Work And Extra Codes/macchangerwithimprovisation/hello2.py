
#editor run with python 2.7 user input with subprocess using list arguments
#terminal run with python3
import subprocess

interface = input("interface >  ")
new_mac = input("new MAC > ")

print("[+] changing MAC address for " + interface + " to  new_mac")


subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])


