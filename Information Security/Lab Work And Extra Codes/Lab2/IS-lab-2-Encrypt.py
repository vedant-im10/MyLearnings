# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 14:23:21 2021

@author: vedpa
"""

def encrypt(text, key): 
    cipher = ''
    for char in text:
        if char == ' ':
            cipher = cipher + char 
        elif char.isupper():
            cipher = cipher + chr((ord(char) + key - 65) % 26 + 65)
        else:
            cipher = cipher + chr((ord(char) + key - 97) % 26 + 97) 
    return cipher

text = input("Enter Message: ") 

s = int(input("Enter Key: "))

print("Cipherd Text: ", encrypt(text, s))