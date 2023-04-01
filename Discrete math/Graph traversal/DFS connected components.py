class Graph:
    def __init__(self,V):
        self.V=V
        #pointer to an array containing adjacency list
        self.adj=[[] for i in range(self.V)]

    def NumberofConnectedComponents(self):
        visited=[False for i in range(self.V)]
        count=0
        for v in range(self.V):
            if visited[v]==False:
                self.DFSuntil(v,visited)
                count+=1
        return count
    
    def DFSuntil(self,v,visited):
        visited[v]=True
        for i in self.adj[v]:
            if not visited[i]:
                self.DFSuntil(i,visited)
    
    def addEdge(self,v,w):
        self.adj[v].append(w)
        self.adj[w].append(v)

if __name__=='__main__':
     
    g = Graph(6)
    g.addEdge(1, 5)
    g.addEdge(0, 2)
    g.addEdge(2, 4)
     
    print(g.NumberofConnectedComponents())
