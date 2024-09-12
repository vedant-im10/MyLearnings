# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 16:43:46 2021

@author: vedpa
"""

import pandas as pd

# Taking NFA input from User 
nfa = {}                                 
n = int(input("No. of states : "))            #Enter total no. of states
t = int(input("No. of transitions : "))       #Enter total no. of transitions/paths eg: a,b so input 2 for a,b,c input 3
for i in range(n):  
    state = input("State name : ")            #Enter state name eg: A, B, C, q1, q2 ..etc
    nfa[state] = {}                           #Creating a nested dictionary
    for j in range(t):
        path = input("path : ")               #Enter path eg : a or b in {a,b} 0 or 1 in {0,1}
        print("Enter end state from state {} travelling through path {} : ".format(state,path))
        reaching_state = [x for x in input().split()]  #Enter all the end states
        nfa[state][path] = reaching_state     #Assigning the end states to the paths in dictionary

print("\nNFA :- \n")
print(nfa)                                    #Printing NFA
print("\nPrinting NFA table :- ")
nfa_table = pd.DataFrame(nfa)
print(nfa_table.transpose())

print("Enter final state of NFA : ")
nfa_final_state = [x for x in input().split()]   #Enter final state/states of NFA               
    
new_states_list = []   #Holds all the new states created in dfa
dfa = {}   #dfa dictionary
keys_list = list(list(nfa.keys())[0])   #conatins all states in nfa and states created in dfa
path_list = list(nfa[keys_list[0]].keys())   #list of all the paths eg: [a,b] or [0,1]

# Computing first row of DFA transition table
dfa[keys_list[0]] = {}   #creating a nested dictionary in dfa 
for y in range(t):
    var = "".join(nfa[keys_list[0]][path_list[y]])   #creating single string of all elements in list in new state
    dfa[keys_list[0]][path_list[y]] = var            #assigning state in DFA table
    if var not in keys_list:                         #if the state is newly created 
        new_states_list.append(var)                  #then append it to the new_states_list
        keys_list.append(var)                        #as well as to the keys_list which contains all the states

# Computing the other rows of DFA transition table
while len(new_states_list) != 0:                     #consition is true only if the new_states_list is not empty
    dfa[new_states_list[0]] = {}                     #taking the first element of the new_states_list and examining it
    for _ in range(len(new_states_list[0])):
        for i in range(len(path_list)):
            temp = []                                #creating a temporay list
            for j in range(len(new_states_list[0])):
                temp += nfa[new_states_list[0][j]][path_list[i]]  #taking the union of the states
            s = ""
            s = s.join(temp)                         #creating a single string(new state) from all the elements of the list
            if s not in keys_list:                   #if the state is newly created
                new_states_list.append(s)            #then append it to the new_states_list
                keys_list.append(s)                  #as well as to the keys_list which contains all the states
            dfa[new_states_list[0]][path_list[i]] = s   #assigning the new state in the DFA table
        
    new_states_list.remove(new_states_list[0])   #Remove first element in new_states_list

print("\nDFA :- \n")    
print(dfa)   #Printing the DFA created
print("\nPrinting DFA table :- ")
dfa_table = pd.DataFrame(dfa)
print(dfa_table.transpose())

dfa_states_list = list(dfa.keys())
dfa_final_states = []
for x in dfa_states_list:
    for i in x:
        if i in nfa_final_state:
            dfa_final_states.append(x)
            break
        
print("\nFinal states of the DFA are : ",dfa_final_states)   #Printing Final states of DFA