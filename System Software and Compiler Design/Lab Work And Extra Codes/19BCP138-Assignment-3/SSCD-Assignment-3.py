# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 23:09:24 2021

@author: vedpa
"""

from itertools import takewhile

def group(lst):
    a = {}
    lst = [m[0] for m in rules]
    initial = list(set(lst))
    for m in initial:
        for i in rules:
            if i.startswith(m):
                if m not in a:
                    a[m] = []
                a[m].append(i)
    return a

def prefix(n):
    return len(set(n)) == 1

start = ""
rules = []
common = []
alphabets = ["A'", "B'", "C'", "D'", "E'", "F'", "G'", "H'", "I'", "J'", "K'", "L'","M'", "N'", "O'", "P'", "Q'", "R'", "S'", "T'", "U'", "V'", "W'", "X'","Y'", "Z'"]

s = input("Grammar: ")
while (True):
    split = s.split("->")
    start = split[0]
    for i in split[1].split("|"):
        rules.append(i)

#Code to remove commons 
    for d, e in group(rules).items():
        r = [e[0] for e in takewhile(prefix, zip(*e))]
        common.append(''.join(r))

    for i in common:
        newalphabet = alphabets.pop()
        print(start + "->" + i + newalphabet)
        index = []
        for d in rules:
            if (d.startswith(i)):
                index.append(d)
        print(newalphabet + "->", end="")
        for j in index:
            printstring = j.replace(i, "", 1) + "|"
            if printstring == "|":
                print("\u03B5" + "|", end="")
            else:
                print(j.replace(i, "", 1) + "|", end="")
        print("\b")
        print("")

    print("\nAnother Grammar ?")
    choice = input("Enter 0 for No and 1 for Yes: ")
    if choice == '1':
        s = input("Enter the Grammar: ")
    if choice == '0':
        break