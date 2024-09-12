import re

import pandas as pd

def splitter(test_list,valu):
    
    if valu in test_list:
        size = len(test_list) 
        idx_list = [idx + 1 for idx, val in
                    enumerate(test_list) if val == valu] 
          
          
        test_list = [test_list[i: j] for i, j in
                zip([0] + idx_list, idx_list + 
                ([size] if idx_list[-1] != size else []))] 
        
        for i in test_list:
            if valu in i:
                i.remove(valu)
    else:
        test_list = [test_list]
        
    return test_list


def parse(user_input,start_symbol,parsingTable):

    #flag
    flag = 0

    #appending dollar to end of input
    user_input = user_input + "$"

    stack = []
    
    stack.append("$")
    stack.append(start_symbol)

    input_len = len(user_input)
    index = 0

    
    while len(stack) > 0:

        #element at top of stack
        top = stack[len(stack)-1]

        print ("Top =>",top)

        #current input
        current_input = user_input[index]

        print ("Current_Input => ",current_input)

        if top == current_input:
            stack.pop()
            index = index + 1    
        else:    

            #finding value for key in table
            key = top , current_input
            print (key)

            #top of stack terminal => not accepted
            if key not in parsingTable:
                flag = 1        
                break

            value = parsingTable[key]
            if value !='@':
                value = value[::-1]
                value = list(value)
                
                #poping top of stack
                stack.pop()

                #push value chars to stack
                for element in value:
                    stack.append(element)
            else:
                stack.pop()        

    if flag == 0:
        print ("String accepted !")
    else:
        print ("String not accepted!")    



def ll1(follow, productions):
    
    print ("\nParsing Table\n")

    table = {}
    for key in productions:
        for value in productions[key]:
            for element in firstRhs_dict[str(value)]:
                if(element!='@'):
                    table[key, element] = value
                    
        if('@' in first(key, productions)):
            for element in follow[key]:
                table[key, element] = ['@']

    for key,val in table.items():
        print (key,"=>",val)

    new_table = {}
    for pair in table:
        new_table[pair[1]] = {}

    for pair in table:
        new_table[pair[1]][pair[0]] = table[pair]


    print ("\n")
    print ("\nParsing Table in matrix form\n")
    print (pd.DataFrame(new_table).fillna('-'))
    print ("\n")

    return table


def follow(s, productions, ans):
    if len(s) != 1:
        return {}

    for key in productions:   
        for value in productions[key]:
            # print(value)
            if(s in value):
                f=value.index(s)
            else: f=-1
            
            if f != -1:
                if f == (len(value) - 1):
                    if key != s:
                        if key in ans:
                            temp = ans[key]
                        else:
                            ans = follow(key, productions, ans)
                            temp = ans[key]
                        ans[s] = ans[s].union(temp)
                else:
                    # print(value,value[f + 1:],'val')
                    fid=0
                    while((f+fid)<len(value)-1):
                        if(value[f +fid + 1:][0].isupper()):
                            
                            first_of_next = first(value[f +fid + 1:][0], productions)
                            
                            ans[s] = ans[s].union(first_of_next) - {'@'}
                            
                            if '@' in first_of_next:
                                fid+=1
                            else: 
                                break
                                
                            
                        else:
                            ans[s] = ans[s].union(value[f+fid + 1:][0])
                            break
                    else:
                        if key != s:
                            if key in ans:
                                temp = ans[key]
                            else:
                                ans = follow(key, productions, ans)
                                temp = ans[key]
                            ans[s] = ans[s].union(temp)
                                    
    return ans


def first(s, productions):
    
    ans = set()
    
    for i in range(len(productions[s])):
        idx=0
        tempset=set()
        while(idx < len(productions[s][i])):
            c = productions[s][i][idx]
            
            if c.isupper():
                
                f = first(c, productions)
                ans = ans.union(x for x in f)               
                tempset = tempset.union(x for x in f)
                
                contflag=0
                for pro in productions[c]:
                    if('@' in pro):   
                        contflag=1
                
                if(contflag==1):idx+=1
                else:break
                
            else:      
                ans = ans.union(c)   
                tempset = tempset.union(c)
                break
        firstRhs_dict[str(productions[s][i])] = firstRhs_dict[str(productions[s][i])].union(tempset)
    return ans


if __name__ == "__main__":
    productions = dict()
    grammar = open("file.txt", "r")
   
    
    
    first_dict = dict()
    follow_dict = dict()
    
    flag = 1
    start = ""
    for line in grammar:
        # l = re.split("( |->|\n|\||)*", line)
        l = re.split("( |->|\n|)*", line)
        #print(l)
        m=[]
        for i in l:
            if i=="":
                pass
            else:
                m.append(i)

        print(m)
        lhs = m[0]
        #print("LHS", lhs)
        rhs = m[1::]
        #print("RHS",rhs)
        if flag:
            flag = 0
            start = lhs
        productions[lhs] = rhs
        
     
    for z in productions.keys():
        productions[z] = splitter(productions[z],'|')
    
    # For tracking first with rhs
    firstRhs_dict = {str(i):set() for rhs in productions.values() for i in rhs}
    
    
    print("PROD", productions)
    
    print('\nFIRST\n')
    for lhs in productions:
        first_dict[lhs] = first(lhs, productions)

    for f in first_dict:
        print(str(f) + " : " + str(first_dict[f]))
    
    # print('first_rhs_dict',firstRhs_dict)    
    # print(first_dict)
        
    print()
    print('\nFollow\n')


    for lhs in productions:
        follow_dict[lhs] = set()
    
    follow_dict[start] = follow_dict[start].union('$')
    
    for lhs in productions:
        follow_dict = follow(lhs, productions, follow_dict)

    for f in follow_dict:
        print(str(f) + " : " + str(follow_dict[f]))

    ll1Table = ll1(follow_dict, productions)

    #parse("a*(a+a)",start,ll1Table)
    parse("ad",start,ll1Table)