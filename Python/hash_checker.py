#!/usr/bin/python

# Created by: shyraffy
# This script takes a file and a hash as an input and checks whether the file hash
# is the same as the input hash

import hashlib
import os
import argparse
import sys

#This function outputs the hash digest of the file in hexadecimal according to he hash type passed
def generate_hash(file_name, algorithm):
    #Throws an exception if the hash type doesn't exits!
    h = hashlib.new(algorithm)

    try:
        with open(file_name, 'rb') as file:
            chunk = 0
            while(chunk != b''):
                #Reads 4KiB of data at a time
                chunk = file.read(4096)
                h.update(chunk) 

        return h.hexdigest()
        
    except FileNotFoundError:
        print("\033[91mError: \033[0mThe file does not exists!")
        sys.exit(1)

def check(file_hash, hash):
    if(file_hash == hash):
        print("The file's hash matches with the input hash!")
    else:
        print("The file's hash does not match with the input hash!")

def main():

    parser = argparse.ArgumentParser(description='File checksum checker')
    parser.add_argument('-f','--file', help='Input file', required='true')
    parser.add_argument('-H', '--hash', metavar='', help='Checksum to test')
    parser.add_argument('-A', '--algorithm', metavar='', help='Hash algorithm')
    args = parser.parse_args()

    algorithm = args.algorithm.lower()

    generated_hash = generate_hash(args.file, algorithm)
    check(generated_hash, args.hash)

if __name__ == "__main__":
    main()