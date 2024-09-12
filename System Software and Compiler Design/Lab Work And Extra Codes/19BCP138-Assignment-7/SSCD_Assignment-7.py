# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 10:22:14 2021

@author: vedpa
"""

import sys


with open("Input-Text.txt") as inputFile:
    contents= inputFile.read()
    
    #Declaring list of all Productions, Variables and Terminals
    grammar = []
    terminals = set()
    variables = set()
    
    #Getting the list of all the Productions
    grammar = contents.split('\n')
    
    #Getting the list of all the Terminals
    for production in grammar:
        for letter in production:
            temp = ord(letter)
            if (temp >= 97 and temp <= 122) or (temp >= 40 and temp <= 43):
                terminals.add(chr(temp))
    
    #Getting the list of all the Variables
    for production in grammar:
        for letter in production:
            temp = ord(letter)
            if temp >= 65 and temp <= 90:
                variables.add(chr(temp))

    print("Grammar is : ", grammar)
    print("Terminals are : ", terminals)
    print("Variables are : ", variables)

g=[]

for production in grammar:
    v=production[0]
    production=production[3:]
    exp=""
    for letter in production:
        if letter!='/':
            exp+=letter
            
        else:
            g.append(v+"->"+exp)
            exp=""
    if exp!="":
        g.append(v+"->"+exp)
#print(g)
for production in g:
    production=production[3:]
    var=False
    for letter in production:
        if letter in variables and var==False:
            var=True
        elif letter in variables or letter=='$':
            sys.exit("\nGrammar is not an operator grammar")
        elif letter in terminals:
            var=False
print("\nGrammar is operator grammar")

dict={}

def leading(v):
    if v in dict.keys():
        return dict[v]
    else:
        dict[v]=[]
    p=[]
    for production in g:
        if production[0]==v:
            p.append(production[3:])
    #print(p)
    #print('\n')
    for pr in p:
        var=False
        if pr[0] in variables:
            var=True
            if pr[0]!=v:
                l=leading(pr[0])
                for each in l:
                    dict[v].append(each)
                dict[v]=list(set(dict[v]))
                #print("******")
                #print(dict)
        elif pr[0] in terminals:
            dict[v].append(pr[0])
        if var==True and len(pr)>1:
            dict[v].append(pr[1])
            #print(dict)
    dict[v]=list(set(dict[v]))
    return dict[v]

dict1={}
    
def trailing(v):
    if v in dict1.keys():
        return dict1[v]
    else:
        dict1[v]=[]
    p=[]
    for production in g:
        if production[0]==v:
            p.append(production[3:])
    for pr in p:
        var=False
        if pr[-1] in variables:
            var=True
            if pr[-1]!=v:
                t=trailing(pr[-1])
                for each in t:
                    dict1[v].append(each)
                dict1[v]=list(set(dict1[v]))
        elif pr[-1] in terminals:
            dict1[v].append(pr[-1])
        if var==True and len(pr)>1:
            dict1[v].append(pr[-2])
    dict1[v]=list(set(dict1[v]))
    return dict1[v]

print("\nNon-Terminal".ljust(16), "Leading".ljust(25), "Trailing".ljust(25))
for v in variables:
    print(v.ljust(15), str(set(leading(v))).ljust(25), str(set(trailing(v))).ljust(25))
