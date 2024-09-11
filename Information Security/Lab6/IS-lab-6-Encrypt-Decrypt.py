# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 14:03:12 2021

@author: vedpa
"""

key=input("Enter a key:- ")
key=key.replace(" ", "")
key=key.upper()
def matrix(x,y,initial):
    return [[initial for i in range(x)] for j in range(y)]
    
result=list()
for char in key: 
    if char not in result:
            result.append(char)
            
for i in range(65,91): 
    if chr(i) not in result:
            result.append(chr(i))

for i in range(48,58):
    result.append(chr(i))

k=0
my_matrix=matrix(6,6,0) 
for i in range(0,6): 
    for j in range(0,6):
        my_matrix[i][j]=result[k]
        k+=1

def locindex(char): 
    loc=list()
    for i ,j in enumerate(my_matrix):
        for k,l in enumerate(j):
            if char==l:
                loc.append(i)
                loc.append(k)
                return loc
            
def encryption():  
    plain_text=str(input("Enter your message:- "))
    msg=plain_text.upper()
    msg=msg.replace(" ", "")             
    i=0
    for s in range(0,len(msg)+1,2):
        if s<len(msg)-1:
            if msg[s]==msg[s+1]:
                msg=msg[:s+1]+'X'+msg[s+1:]
    if len(msg)%2!=0:
        msg=msg[:]+'X'
    print("Encrypted text is :-",end=' ')
    while i<len(msg):
        loc=list()
        loc=locindex(msg[i])
        loc1=list()
        loc1=locindex(msg[i+1])
        if loc[1]==loc1[1]:
            print("{}{}".format(my_matrix[(loc[0]+1)%6][loc[1]],my_matrix[(loc1[0]+1)%6][loc1[1]]),end=' ')
        elif loc[0]==loc1[0]:
            print("{}{}".format(my_matrix[loc[0]][(loc[1]+1)%6],my_matrix[loc1[0]][(loc1[1]+1)%6]),end=' ')  
        else:
            print("{}{}".format(my_matrix[loc[0]][loc1[1]],my_matrix[loc1[0]][loc[1]]),end=' ')    
        i=i+2        
                 
def decryption():  
    msg=str(input("\nEnter your encrypted text :- "))
    msg=msg.upper()
    msg=msg.replace(" ", "")
    print("Decrypted text is :-",end=' ')
    i=0
    while i<len(msg):
        loc=list()
        loc=locindex(msg[i])
        loc1=list()
        loc1=locindex(msg[i+1])
        if loc[1]==loc1[1]:
            print("{}{}".format(my_matrix[(loc[0]-1)%6][loc[1]],my_matrix[(loc1[0]-1)%6][loc1[1]]),end=' ')
        elif loc[0]==loc1[0]:
            print("{}{}".format(my_matrix[loc[0]][(loc[1]-1)%6],my_matrix[loc1[0]][(loc1[1]-1)%6]),end=' ')  
        else:
            print("{}{}".format(my_matrix[loc[0]][loc1[1]],my_matrix[loc1[0]][loc[1]]),end=' ')    
        i=i+2        

encryption()
decryption()