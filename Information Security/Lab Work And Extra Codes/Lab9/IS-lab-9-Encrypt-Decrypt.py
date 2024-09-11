# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 19:39:38 2021

@author: vedpa
"""

import rsa
from sympy.crypto.crypto import encipher_vigenere,decipher_vigenere
from sympy.crypto.crypto import encipher_hill,decipher_hill
from sympy import Matrix

message = input("Enter Message: ")
print("Original string: ", message)

#Assymmetric-key (RSA) Algorithm
publicKey, privateKey = rsa.newkeys(512)
encryptMessage = rsa.encrypt(message.encode(),publicKey)
print("\nAsymmetric-key Encryption (RSA): ", encryptMessage)
decryptMessage = rsa.decrypt(encryptMessage, privateKey).decode()
print("Asymmetric-key Dencryption: ", decryptMessage)

#Vigenere Algorithm
vigenere_encrypt = encipher_vigenere(message, "ved")
print("\nEncryption by Vigenere algorithm (RSA): ",vigenere_encrypt)
vigenere_decrypt = decipher_vigenere(vigenere_encrypt, "ved")
print("Decryption by Vigenere algoithm: ",vigenere_decrypt)

#Hill Cypher Algorithm
hill_key = Matrix([[1,2,3],[0,1,4],[5,6,0]])
hill_encrypt = encipher_hill(message, hill_key)
print("\nEncryption by Hill algorithm: ",hill_encrypt)
hill_decrypt = decipher_hill(hill_encrypt, hill_key)
print("Decryption by Hill algoithm: ",hill_decrypt)
