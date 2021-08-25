#!/usr/bin/env python

# Author: shyraffy
# Very simple mac changer script
# Only compatible with linux


import subprocess 
import optparse 
import re
import random

# Command-line arguments handling
def get_args():
    parser = optparse.OptionParser() # Creates the parser object

    parser.add_option('-i', '--interface', dest='interface', help='Interface to change its MAC')
    parser.add_option('-a', '--address', dest='new_address', help='New MAC address')
    parser.add_option('-r', '--random', dest='random_address', action='store_true', help='Generates a random MAC address')
    

    options, arguments = parser.parse_args() 

    if not options.interface:
        parser.error('[-] You must specify an interface! Use --help for more info')
    
    elif not options.new_address:
        parser.error('[-] You must specify an address! Use --help for more info')


    return options

def get_mac_address(interface):

    ifconfig_output = subprocess.check_output(['ifconfig', interface])

    #Finds the mac address on the ifconfig output
    current_mac = re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', str(ifconfig_output))

    #If it was found, return it
    if(current_mac):
        return current_mac.group(0)


def change_mac(interface, new_address):
    print("[+] Changing MAC address for " + interface + " to " + new_address)

    #Changes the mac
    subprocess.call(['ifconfig', interface, 'down'])
    subprocess.call(['ifconfig', interface, 'hw', 'ether', new_address])
    subprocess.call(['ifconfig', interface, 'up'])

        
    if(new_address == get_mac_address(interface)):
        print('[+] MAC successfully changed to ' + new_address)
    else:
        print('[-] ERROR: Could not change MAC address')

if __name__ == "__main__":
    options = get_args()

    current_mac = get_mac_address(options.interface)

    if(current_mac != None): 

        if(current_mac == options.new_address):
            print('[!] The interface already has the specified MAC address!')
        else:
            print('[+] Current MAC adress: ' + current_mac)
            change_mac(options.interface, options.new_address)
    else:
        print('[-] ERROR: Could not read MAC address')


