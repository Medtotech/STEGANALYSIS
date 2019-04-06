#Evelyn Okougbo
#Password cracker using bruteforce
#10/09/2018

import md5
import hashlib



small = 'abcdefghijklmopqrstuvwxyz'
big = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = '0123456789'

characters = []
characters = small + num + big


def password_hacker():
    #loop to genrate possible combinations of characters
    for i in characters:
        for j in characters:
            for k in characters:
                for l in characters:
                    for m in characters:
                        tool = i+j+k+l+m
                        
                        #hash character combination
                        hasher= hashlib.md5(tool)
                        hashed= hasher.hexdigest() 

                        #check if generated hash values matches known hash
                        if hashed =="e076e7960533c2a998b91fa7c76fda2a":
                            print ("The password to Jkirk.zip is: " + tool)

                        elif hashed == "37f2dbe5ec3f01f5f70b5ef61d37cdc5" :
                            print ("The password to Lmccoy.zip is: " + tool)
                        

                        elif hashed == "ae6e27cef852717bb3127bd0b6d2e6ef" :
                            print ("The password to Cchapel.zip is: " + tool)
                            
                        else:
                            continue

password_hacker()        
