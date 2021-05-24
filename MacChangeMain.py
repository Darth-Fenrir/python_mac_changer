#!/usr/bin/env python

# Imported packages
import subprocess
import optparse
import re

# Logic function
def get_arguments():
    # Parser for command line interface
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="mac_address", help="Specify a new MAC address")
    # Variable's
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info")
    elif not options.mac_address:
        parser.error("[-] Please specify a new MAC address, use --help for more info")
    return options

def change_mac(interface, mac_address):
    print("Changing " + interface + " MAC address to " + mac_address)
    subprocess.call(["sudo", "ifconfig", interface, "down"])
    subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", mac_address])
    subprocess.call(["sudo", "ifconfig", interface, "up"])

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read MAC address.")

# Function calls
options = get_arguments()

current_mac = get_current_mac(options.interface)
print("Current MAC is = " + str(current_mac))
change_mac(options.interface, options.mac_address)

current_mac = get_current_mac(options.interface)
if current_mac == options.mac_address:
    print("[+] MAC address was successfully changed to " + current_mac)
else:
    print("[-] MAC address did not get changed.")
