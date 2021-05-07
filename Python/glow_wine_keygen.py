#!/usr/bin/python

# Created by: shyraffy
# This script is a keygen I made for cracking this binary: https://crackmes.one/crackme/5df26b4033c5d419aa013362

import random
import sys
import platform


def check_key(key):
    sum = 0
    result = -1
    #Adds the ASCII value of each letter together
    for char in key:
        sum += ord(char)

    if (sum == 300):
        result = 1

    return result

def generate_key(amount):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet += alphabet.upper()
    i = 1

    while (i <= amount):
        key = ""
        #Generates the key
        while len(key) < 3:
            key += random.choice(alphabet)

        #If the key is found
        if(check_key(key) == 1):
            #The first character can be any letter
            key = random.choice(alphabet) + '@' + key
            print("Key Found!: " + key)
            i += 1
   
       
if __name__ == "__main__":
    #Wrong arg parssing
    if(len(sys.argv) != 2):
        if(platform.system() == "Linux"):
            print("Usage: ./glow_wine_keygen <number of keys>")
        else:
            print("Usage: py glow_wine_keygen <number of keys>")
    else:
        generate_key(int(sys.argv[1]))



