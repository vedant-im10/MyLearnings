# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 09:26:19 2021

@author: vedpa
"""

with open("Input.txt") as inputFile:
    contents= inputFile.read()
    
    #Declaring list of all Productions, Variables and Terminals
    productions = []
    terminals = set()
    variables = set()
    
    #Getting the list of all the Productions
    productions = contents.split('\n')
    
    #Getting the list of all the Terminals
    for production in productions:
        for letter in production:
            temp = ord(letter)
            if (temp >= 97 and temp <= 122) or temp == 64 or (temp >=40 and temp <= 43):
                terminals.add(chr(temp))
    
    #Getting the list of all the Variables
    for production in productions:
        for letter in production:
            temp = ord(letter)
            if temp >= 65 and temp <= 90:
                variables.add(chr(temp))

    print("Production is : ", productions)
    print("Terminals are : ", terminals)
    print("Variables are : ", variables)

f={} #First
fw={} #Follow
done=[] #For First
done_follow=[] #For Follow

#Productions
print("\nProductions in the grammar are : ")
for production in productions:
    print(production)
print()

#First and follow
print("First and Follow:")
print("Terminal".ljust(15), "First".ljust(25), "Follow".ljust(25))

#Calculating First for the Grammar
def first(variable):
    
    pr=[] #Appending the right side of Productions in the List
    flag=0 
    if variable not in done:
        for production in productions:
            if production[0]==variable:
                pr.append(production[3:])
    else:
        return f[variable]
    
    f[variable]=[]
    
    for production in pr:
        fir=True
        for letter in production:
            if letter==variable and fir:
                fir=False
            elif (letter!=variable) and (letter in variables) and (fir or flag==1):
                temp=first(letter) #Calculating first of that Letter
                if "@" not in temp:
                    flag=0
                if letter=='/' and flag==1:
                    flag=0
                    f[variable].append('@')
                for each in temp:
                    if each=='@':
                        flag=1
                    else:
                        f[variable].append(each)
                fir=False
            elif (letter in terminals) and (fir or flag==1):
                f[variable].append(letter)
                flag=0
                fir=False
            elif letter=='/':
                fir=True
                if flag==1:
                    f[variable].append('@')
                    flag=0
        if flag==1:
            f[variable].append('@')
    done.append(variable)
    return f[variable]

#Calculating Follow for the Grammar
def follow(variable):
    if variable in done_follow:
        return fw[variable]
    fw[variable]=[]
    if variable==productions[0][0]:
        fw[variable].append('$')
        
    for production in productions:
        rhs=production[3:]
        flag=0
        if variable in rhs:
            for letter in rhs:
                if letter==variable and flag==0:
                    flag=1
                elif (letter in variables) and flag==1:
                    temp=first(letter)
                    for each in temp:
                        if each!='@':
                            fw[variable].append(each)
                    if '@' not in temp:
                        flag=0
                elif (letter in terminals) and flag==1:
                    fw[variable].append(letter)
                    flag=0
                elif letter=='/' and flag==1:
                    if variable!=production[0]:
                        temp=follow(production[0])
                        for each in temp:
                            fw[variable].append(each)
                    flag=0
        if flag==1:
            if variable!=production[0]:
                temp=follow(production[0])
                for each in temp:
                    fw[variable].append(each)
    done_follow.append(variable)
    return fw[variable]

for v in variables:
    print(v.ljust(15), str(set(first(v))).ljust(25), str(set(follow(v))).ljust(25))
