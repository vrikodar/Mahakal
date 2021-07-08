#By SxNade
#https://github.com/SxNade/Mahakal
#CONTRIBUTE
#Author z3r0day

import hashlib
import os
import sys
import time
from termcolor import colored
#importing the required libraries

golo = '''
    ...     ..      ..                                               ..                        .. 
  x*8888x.:*8888: -"888:                 .uef^"                < .z@8"`                  x .d88"  
 X   48888X `8888H  8888               :d88E                    !@88E                     5888R   
X8x.  8888X  8888X  !888>        u     `888E             u      '888E   u          u      '888R   
X8888 X8888  88888   "*8%-    us888u.   888E .z8k     us888u.    888E u@8NL     us888u.    888R   
'*888!X8888> X8888  xH8>   .@88 "8888"  888E~?888L .@88 "8888"   888E`"88*"  .@88 "8888"   888R   
  `?8 `8888  X888X X888>   9888  9888   888E  888E 9888  9888    888E .dN.   9888  9888    888R   
  -^  '888"  X888  8888>   9888  9888   888E  888E 9888  9888    888E~8888   9888  9888    888R   
   dx '88~x. !88~  8888>   9888  9888   888E  888E 9888  9888    888E '888&  9888  9888    888R   
 .8888Xf.888x:!    X888X.: 9888  9888   888E  888E 9888  9888    888E  9888. 9888  9888   .888B . 
:""888":~"888"     `888*"  "888*""888" m888N= 888> "888*""888" '"888*" 4888" "888*""888"  ^*888%  
    "~'    "~        ""     ^Y"   ^Y'   `Y"   888   ^Y"   ^Y'     ""    ""    ^Y"   ^Y'     "%    
                                             J88"                                                 
                                             @%     *By SxNade https://github.com/SxNade                                  
                                           :"                 '''


print(golo)
time.sleep(1)
print("Mahakal (v1.1) starting...")
time.sleep(1.4)
supported_hashes = '''
\n
[--Supported Hash Types--]
        *MD5
        *SHA-1
        *SHA-256
        *SHA-512
\n
'''
#printing the supported hash types...--///

print(colored(supported_hashes, 'green'))


if len(sys.argv) != 4:
    print(colored("[*]Usage python3 mahakal.py <hash-value> <hash-type> <path-to-password-file>\n", 'white', attrs=['reverse', 'blink']))
    sys.exit(0)
    #Checking for correct number of arguments

hash_value = sys.argv[1]
hash_type = sys.argv[2]
pass_file = sys.argv[3]
#Receiving the neccessary arguments for cracking the hash value...

if os.path.exists(pass_file) == False:
    print(colored("[!]Password File Not Found...exiting now", "red", attrs=['bold']))
    sys.exit(0)
#Check if the specified password file exists or not...

with open(pass_file, 'r') as file:
    for line in file.readlines():
        #open and read the file containig passwords to check with
        if hash_type == 'md5':
            #condition to check if the hash type is MD5
            hash_object = hashlib.md5(line.strip().encode())
            hashed = hash_object.hexdigest()
            if hashed == hash_value:
                #if the hash_value given equals the hashed_value from passwords at any point print the cracked hash value and exit the program
                print("[*]Initializing Mahakal. . . . .")
                print(colored(f"\n\n[+]MD5 Hash Cracked Successfully------Value = {line.strip()}\n\n", 'green', attrs=['bold']))
                sys.exit(0)

        elif hash_type == 'sha1':
            #condition to check if the hash type is SHA-1
            hash_object = hashlib.sha1(line.strip().encode())
            hashed = hash_object.hexdigest()
            if hashed == hash_value:
                #if the hash_value given equals the hashed_value from passwords at any point print the cracked hash value and exit the program
                print("[*]Initializing Mahakal. . . . .")
                print(colored(f"\n\n[+]SHA-1 Hash Cracked Successfully------Value = {line.strip()}\n\n", 'green', attrs=['bold']))
                sys.exit(0)
        
        elif hash_type == 'sha256':
            #condition to check if the hash type is SHA-256
            hash_object = hashlib.sha256(line.strip().encode())
            hashed = hash_object.hexdigest()
            if hashed == hash_value:
                #if the hash_value given equals the hashed_value from passwords at any point print the cracked hash value and exit the program
                print("[*]Initializing Mahakal. . . . .")
                print(colored(f"\n\n[+]SHA-256 Hash Cracked Successfully------Value = {line.strip()}\n\n", 'green', attrs=['bold']))
                sys.exit(0)

        elif hash_type == 'sha512':
            #condition to check if the hash type is SHA-512
            hash_object = hashlib.sha512(line.strip().encode())
            hashed = hash_object.hexdigest()
            if hashed == hash_value:
                #if the hash_value given equals the hashed_value from passwords at any point print the cracked hash value and exit the program
                print("[*]Initializing Mahakal. . . . .")
                print(colored(f"\n\n[+]SHA-512 Hash Cracked Successfully------Value = {line.strip()}\n\n", 'green', attrs=['bold']))
                sys.exit(0)
        
    print(colored("\n[*]Please Consider Changing your wordlist of passwords\n", 'red', attrs=['bold']))
    print(print(colored("\n\n[!]Incorrect or Unsupported Hash Type or Password Not Found \n\n", 'red', attrs=['bold'])))
    print(print(colored("\n[*]Please Recheck the arguments you gave\n", 'red', attrs=['bold'])))
    sys.exit(0)
    #this is really annoying --- check your arguments--!Oh!

