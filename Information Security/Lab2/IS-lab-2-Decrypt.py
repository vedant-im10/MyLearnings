# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 14:24:24 2021

@author: vedpa
"""

def decrypt(text, key):
    decipher = ''
    for char in text: 
        if char == ' ':
            decipher = decipher + char 
        elif char.isupper():
            decipher = decipher + chr((ord(char) - key - 65) % 26 + 65) 
        else:
            decipher = decipher + chr((ord(char) - key - 97) % 26 + 97)
    return decipher

text = input("Enter Message: ")

s = int(input("Enter Key: "))

print("Decipherd Text: ", decrypt(text, s))