# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 11:38:36 2021

@author: vedpa
"""

#Encryption
def encrypt(text, key):
  encryption = [[" " for i in range(len(text))] for j in range(key)]
  flag = None
  row = 0
  for i in range(len(text)):
    encryption[row][i] = text[i]
    if row == 0:
      flag = True
    elif row == key-1:
      flag = False
    if flag:
      row += 1
    else:
      row -= 1

  for i in range(key):
    print("".join(encryption[i]))

  ct=[]
  for i in range(key):
    for j in range(len(text)):
      if encryption[i][j] != ' ':
        ct.append(encryption[i][j])
  return("".join(ct))

text = input("Enter string: ")
key = int(input("Enter key: "))
print("Ciphered text is: ", encrypt(text, key))