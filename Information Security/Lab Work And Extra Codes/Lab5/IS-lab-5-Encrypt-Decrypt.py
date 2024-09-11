# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 10:30:07 2021

@author: vedpa
"""

def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string) - len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))

def encrypt(string, key):
    encrypt_text = []
    for i in range(len(string)):
        x = (ord(string[i]) + ord(key[i])) % 26
        x += ord('A')
        encrypt_text.append(chr(x))
    return("" . join(encrypt_text))

def decrypt(encrypt_text, key):
    decrypt_text = []
    for i in range(len(encrypt_text)):
        x = (ord(encrypt_text[i]) - ord(key[i]) + 26) % 26
        x += ord('A')
        decrypt_text.append(chr(x))
    return("" . join(decrypt_text))
    
# Driver code
if __name__ == "__main__":
    string = input("Enter the text: ")
    keyword = input("Enter a key: ")
    key = generateKey(string, keyword)
    encrypt_text = encrypt(string, key)
    choice = int(input("Choose 1 to Encrypt and 2 to Decrypt(Vigenere Cipher):"))
    if choice == 1:
        print("\nEncrypted text is:", encrypt_text)
    elif choice == 2:
        print("\nDecryped Message is:", decrypt(string,key))
    else:
        print("Please Enter A Valid Number")
