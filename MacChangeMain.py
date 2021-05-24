#!/usr/bin/env python

# Imported packages
import subprocess
import optparse

# Parser for command line interface
parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
parser.add_option("-m", "--mac", dest="mac_address", help="Specify a new MAC address")

# Variable's
(options, arguments) = parser.parse_args()
interface = options.interface
mac_address = options.mac_address

# Logic
print("Changing " + interface + " MAC address to " + mac_address)
subprocess.call(["sudo", "ifconfig", interface, "down"])
subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", mac_address])
subprocess.call(["sudo", "ifconfig", interface, "up"])
subprocess.call(["ifconfig"])
