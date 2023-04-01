class Graph:
    def __init__(self,vertices):
        self.V=vertices #No. of vertices
        self.graph=[] #to store graph
    def add_edge(self,u,v,weight):
        self.graph.append([u,v,weight])
    def find_subtree(self,parent,i):
        if parent[i]==i:
            return i
        return self.find_subtree(parent,parent[i])
    def connectsubtree(self,parent,subtree_size,x,y):
        xroot=self.find_subtree(parent,x)
        yroot=self.find_subtree(parent,y)
        if subtree_size[xroot]<subtree_size[yroot]:
            parent[xroot]=yroot
        elif subtree_size[yroot]<subtree_size[xroot]:
            parent[yroot]=xroot
        else:
            parent[yroot]=xroot
            subtree_size[xroot]+=1

    def Kruskal_MST(self):
        result=[]
        i=0 #iterator
        e=0 #number of edges
        self.graph=sorted(self.graph, key=lambda x:x[2])
        parent=[]
        subtree_size=[]
        for node in range(self.V):
            parent.append(node)
            subtree_size.append(0)
        while e<self.V-1:
            node1,node2,weight=self.graph[i]
            i+=1
            x=self.find_subtree(parent,node1)
            y=self.find_subtree(parent,node2)
            if x!=y:
                e+=1
                result.append([node1,node2,weight])
                self.connectsubtree(parent,subtree_size,x,y)
        for node1,node2,weight in result:
            print('%d-%d:%d' %(node1,node2,weight))
example_graph = Graph(9)
example_graph.add_edge(7, 6, 1)
example_graph.add_edge(8, 2, 2)
example_graph.add_edge(6, 5, 2)
example_graph.add_edge(0, 1, 4)
example_graph.add_edge(2, 5, 4)
example_graph.add_edge(8, 6, 6)
example_graph.add_edge(2, 3, 7)
example_graph.add_edge(7, 8, 7)
example_graph.add_edge(0, 7, 8)
example_graph.add_edge(1, 2, 8)
example_graph.add_edge(3, 4, 9)
example_graph.add_edge(5, 4, 10)
example_graph.add_edge(1, 7, 11)
example_graph.add_edge(3, 5, 14)
example_graph.Kruskal_MST()

