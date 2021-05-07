# Created by: shyraffy
# Date: 29/03/2021
# Inspired by: https://youtu.be/hhUb5iknVJs
# This little program checks if a given password is in the haveibeenpwned database

import hashlib, getpass
from requests import get

# Hashes the password using the SHA1 algorithm
def hash_password(plain_passwd):
    hash = hashlib.new('sha1')
    hash.update(plain_passwd.encode())
    hashed_passwd = hash.hexdigest()

    return hashed_passwd

#Requests to the API to retrieve possible passwords matches 
def check_passwd(hashed_passwd):
    # First 5 characters of the password hash
    hashed_passwd_prefix = hashed_passwd[:5]

    request = get("https://api.pwnedpasswords.com/range/{}".format(hashed_passwd_prefix))

    pwned = False
    ocurrences = 0
    hashes_list = request.text.splitlines()
    for hash_result in hashes_list:

        hash = hashed_passwd_prefix + hash_result[:35]
        if(hashed_passwd == hash):
            pwned = True
            break
    
    if pwned:
        print('\nYour password was pwned!')
        print(f'Hash: {hashed_passwd}, {ocurrences} ocurrences')
    else:
        print('Good news - Password not found!')

    
if __name__ == "__main__":

    print("--Script created by shyraffy in GitHub--")

    plain_passwd = getpass.getpass('\nIntroduce a password: ')
    hashed_passwd = hash_password(plain_passwd).upper()
    check_passwd(hashed_passwd)

