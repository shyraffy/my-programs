# This program takes a list of ip's in form of a file and searchs for
# the location of each one
# This script doesn't really work since whatismyipaddress.com uses a cloufire service which blocks the conection

from requests import get
from bs4 import BeautifulSoup
import re
import time
import sys

def locate_ip(ip):
    request = get("https://whatismyipaddress.com/ip/{}".format(ip))
    country = re.findall("(?<=Country.{15}).+?(?=<)", request.text)
    if len(country) == 0:
        return "Not Found"
    else:
        return country[0]

def main():
    try:
        with open(sys.argv[1], 'r') as ip_list:
            for ip in ip_list:
                country = locate_ip(ip)
                print(str(ip) + "--> " + str(country))
                #For not getting blocked from the site for making to many requests
                time.sleep(1)
    except FileNotFoundError:
        print("\033[91mError: \033[0mThe file does not exists!")

if __name__ == "__main__":
    main()