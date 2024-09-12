import time

class Graph:
    def __init__(self, V, costs):
        self.V = V
        self.costs = costs
        self.adj = {}
        for i in range(self.V):
            self.adj[i] = []

    def add_edge(self, src, dest, isundir=True):
        self.adj[src].append(dest)
        if isundir:
            self.adj[dest].append(src)

    def print_adj_list(self):
        for i in range(self.V):
            print(i, end=" : ")
            for j in self.adj[i]:
                print(j , end=" ")
            print()

    def best_first_search(self, src, goal):
        q = [(src, self.costs[src])]
        visited = [False]*self.V
        visited[src] = True
        while(len(q)):
            # print(q)
            q.sort(key=lambda tup: tup[1])
            f = q[0]
            print(f[0], end=" ")
            q.pop(0)
            if(f[0]==goal): return
            for i in self.adj[f[0]]:
                if visited[i]==False:
                    q.append((i, costs[i]))
                    visited[i] = True

costs=[40, 32, 25, 35, 19, 17, 0, 10]
G = Graph(11, costs)
G.add_edge(0, 1)
G.add_edge(0, 2)
G.add_edge(0, 3)
G.add_edge(1, 4)
G.add_edge(2, 4)
G.add_edge(2, 5)
G.add_edge(3, 5)
G.add_edge(4, 7)
G.add_edge(5, 6)
G.add_edge(7, 6)

costs=[37, 22, 45, 15, 29, 7, 0, 20]
H = Graph(11, costs)
H.add_edge(0, 1)
H.add_edge(0, 2)
H.add_edge(0, 3)
H.add_edge(1, 4)
H.add_edge(2, 4)
H.add_edge(2, 5)
H.add_edge(3, 5)
H.add_edge(4, 7)
H.add_edge(5, 6)
H.add_edge(7, 6)

costs=[27, 12, 25, 5, 19, 2, 0, 10]
I = Graph(11, costs)
I.add_edge(0, 1)
I.add_edge(0, 2)
I.add_edge(0, 3)
I.add_edge(1, 4)
I.add_edge(2, 4)
I.add_edge(2, 5)
I.add_edge(3, 5)
I.add_edge(4, 7)
I.add_edge(5, 6)
I.add_edge(7, 6)

graphs = [G, H, I]

strt = time.time()
for i in graphs:
  i.best_first_search(0, 6)
  print()
end = time.time()
print('\ntime taken in best first search:', (end-strt)/len(graphs))