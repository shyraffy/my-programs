# Created by: shyraffy
# Very simple port scanner using sockets. 
# This program is very low, It would be better to use multi-threading

import argparse
import socket
import os
import platform
import sys
from datetime import datetime

# Argument handling
def arg_parse():
    parser = argparse.ArgumentParser(description = 'Basic port scanner')
    parser.add_argument('-t', '--target', metavar='',required='true', help='Host to scan')
    parser.add_argument('-p', '--port', metavar='', nargs='?' ,help='''Port to scan. If not indicated
                        the most popular ports will be scanned''', default='22,25,53,70,80,443')
    parser.add_argument('-Pn', action='store_true', help="If indicated, the script won't ping the target", default=False)
    parser.add_argument('--open', action='store_true', help='Show only open ports', default=False)
    #parser.add_argument('--O', help='Output fille', default=False)
    #parser.add_argument('-s', action='count', help='Scan speed'. , default=0)
    args = parser.parse_args()

    return args

# Pings the host to know if it's up
def check_host(target):
    # Identifies the OS to know witch parameter to use
    param = '-n' if platform.system()=='Windows' else '-c' 
    response = os.popen(f'ping {param} 1 -w 2 {target}').read() 

    if 'ttl'.upper() in response:                       
        print(f'\nHost {target} is up!')
    else:
        print(f'\nHost {target} is down!')
        sys.exit()
    
def check_ports(target, ports, show_open_only):
    print('\nPort\tStatus\n')
    try:
        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Creates the Socket
            sock.settimeout(3) 

            # Returns an error indicator. If the connection was succesfull, returns a 0
            result = sock.connect_ex((target, int(port))) 
            if (result == 0):
                print(port + '\tOpen')
            else:
                if not show_open_only:
                    print(port,'\tClosed or filtered')
            sock.close()

    except KeyboardInterrupt:
        print("\nExiting program")
        sys.exit()

    except socket.error as error:
        print(str(error) + '\nConection error')
        sys.exit()

def main():
    banner = r"""  
 _____           _      _____                                 
|  __ \         | |    / ____|                                
| |__) |__  _ __| |_  | (___   ___ __ _ _ __  _ __   ___ _ __ 
|  ___/ _ \| '__| __|  \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
| |  | (_) | |  | |_   ____) | (_| (_| | | | | | | |  __/ |   
|_|   \___/|_|   \__| |_____/ \___\__,_|_| |_|_| |_|\___|_|""" 

    print(banner)
    print('-' * 60)
    print('\nTime started: ' + str(datetime.today().strftime('%Y-%m-%d-%H:%M:%S')))

    args = arg_parse()

    ports = args.port.split(',')
    target = socket.gethostbyname(args.target) #Translates hostname to IPV4

    if not args.Pn:
        check_host(target)

    check_ports(target, ports, args.open)

if __name__ == "__main__":
    main()


