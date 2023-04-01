class Graph:
    def __init__(self,vertices):
        self.vertices=vertices
        self.graph=[[0 for i in range(vertices)] for j in range(vertices)]
    def add_edge(self,node1,node2,weight):
        self.graph[node1][node2]=weight
        self.graph[node2][node1]=weight
    def prims_mst(self):
        # Defining a really big number, that'll always be the highest weight in comparisons
        postitive_inf = float('inf')
        # This is a list showing which nodes are already selected 
        # so we don't pick the same node twice and we can actually know when stop looking
        selected_nodes=[False for node in range(self.vertices)]
        
        #Matrix of resulting MST
        result=[[0 for i in range(self.vertices)] for j in range(self.vertices)]
        indx=0
        #for i in range(self.vertices):
            #print(self.graph[i])
        #print(selected_nodes)
        
        # While there are nodes that are not included in the MST, keep looking:
        while(False in selected_nodes):
            # We use the big number we created before as the possible minimum weight
            minimum = postitive_inf

            # The starting node
            start = 0

            # The ending node
            end = 0
            for i in range(self.vertices):
                if selected_nodes[i]:
                    for j in range(self.vertices):
                        # If the analyzed node have a path to the ending node AND its not included in the MST (to avoid cycles)
                        if not selected_nodes[j] and self.graph[i][j]>0:
                            if self.graph[i][j]<minimum:
                                minimum=self.graph[i][j]
                                start,end=i,j
            # Since we added the ending vertex to the MST, it's already selected:
            selected_nodes[end] = True
            # Filling the MST Adjacency Matrix fields:
            result[start][end] = minimum
            if minimum == postitive_inf:
                result[start][end] = 0

            print("(%d.) %d - %d: %d" % (indx, start, end, result[start][end]))
            indx += 1
            result[end][start] = result[start][end]
        # Print the resulting MST
        # for node1, node2, weight in result:
        for i in range(len(result)):
            for j in range(0+i, len(result)):
                if result[i][j] != 0:
                    print("%d - %d: %d" % (i, j, result[i][j]))
example_graph = Graph(9)
example_graph.add_edge(0, 1, 4)
example_graph.add_edge(0, 2, 7)
example_graph.add_edge(1, 2, 11)
example_graph.add_edge(1, 3, 9)
example_graph.add_edge(1, 5, 20)
example_graph.add_edge(2, 5, 1)
example_graph.add_edge(3, 6, 6)
example_graph.add_edge(3, 4, 2)
example_graph.add_edge(4, 6, 10)
example_graph.add_edge(4, 8, 15)
example_graph.add_edge(4, 7, 5)
example_graph.add_edge(4, 5, 1)
example_graph.add_edge(5, 7, 3)
example_graph.add_edge(6, 8, 5)
example_graph.add_edge(7, 8, 12)
example_graph.prims_mst()