# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 11:38:35 2021

@author: vedpa
"""

#Decryption
def decrypt(s, k):
  decryption=[[" " for i in range(len(s))] for j in range(k)]
  flag= None
  row, col = 0, 0

  for i in range(len(s)):
    if row==0:
      flag=True
    elif row==k-1:
      flag=False
    decryption[row][col]= "*"
    col +=1 

    if flag:
      row+=1
    else:
      row-=1
  for i in range(k):
    print("".join(decryption[i]))

  index = 0
  for i in range(k):
    for j in range(len(s)):
      if ((decryption[i][j]=='*') and (index < len(s))):
        decryption[i][j] = s[index]
        index += 1

  dt=[]
  row, col = 0, 0
  for j in range(len(s)):
    if row==0:
      flag=True
    if row==k-1:
      flag=False
     
    if decryption[row][col] !='*':
      dt.append(decryption[row][col])    
      col += 1   

    if flag:
      row+=1
    else:
      row-=1

  return("".join(dt))

s=input("Enter string: ")
k=int(input("Enter key: "))
print("Deciphered text is: ", decrypt(s, k))