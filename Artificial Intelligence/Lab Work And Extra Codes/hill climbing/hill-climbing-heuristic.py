graph = {
    'S' : ['A', 'B'],
    'A' : ['C', 'D'],
    'B' : ['E', 'F'],
    'C' : [],
    'D' : [],
    'E' : ['H'],
    'F' : ['I', 'G'],
    'G' : [],
    'H' : [],
    'I' : []
    }

heuristic = {
    'S' : 13,
    'A' : 12,
    'B' : 4,
    'C' : 7,
    'D' : 3,
    'E' : 8,
    'F' : 2,
    'H' : 4,
    'I' : 9,
    'G' : 0
    }

startstate = input('Enter start state: ')
goalstate = 'G'#input('Enter goal state: ')

curr = startstate
cost = 0

while(True):
    flag=0
    if(curr==goalstate):
        print(curr, "\nsuccess")
        break
    else:
        print(curr, end="->")
    nextNodes = graph[curr]
    for nextNode in nextNodes:
        if(nextNode == goalstate or heuristic[nextNode]<heuristic[curr]):
            curr = nextNode
            flag=1
    if(flag==0):
        print("\nfailure")
        break