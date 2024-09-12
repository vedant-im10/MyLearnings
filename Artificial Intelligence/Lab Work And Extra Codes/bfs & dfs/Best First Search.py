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

OPEN = [startstate]
CLOSED = []

heuristicOrder = sorted(heuristic, key=heuristic.get)

while True:
    if(len(OPEN)==0):
        print("No path")
        break
    node = OPEN.pop(0)
    CLOSED.append(node)
    nextNodes =  graph[node]
    if goalstate in nextNodes:
        CLOSED.append(goalstate)
        print("success")
        print(CLOSED)
        break
    for nextNode in nextNodes:
        if nextNode not in OPEN and nextNode not in CLOSED:
            OPEN.append(nextNode)
    OPEN = [x for _,x in sorted(zip(heuristicOrder, OPEN))]
    
