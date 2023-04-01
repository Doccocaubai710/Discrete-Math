from math import inf
v = 5
graph = [[0, 3, 14, 18,15], [3,0,4,22,20],
             [17, 9, 0, 16,4], [9, 20, 7, 0,18],[9,15,11,5,0]]

path = [0] * (v + 1)
bound = [0] * (v + 1)
for i in range(v):
    bound[i] = 0
for i in range(v):
    for j in range(v):
        if (graph[i][j] != 0):
            bound[i] += graph[i][j]
path[0] = 0
min_cost=inf
for i in range(v):
    for j in range(v):
        if graph[i][j]<min_cost and graph[i][j]>0:
            min_cost=graph[i][j]


def TSP():
   
    min_tour=inf

    min_tour = tsp_bb(graph, v, min_tour, 0, 1, path)

    print("Minimum tour cost: " + str(min_tour))
    print("Tour: " + str(path))
def tsp_bb(graph, v, curr_bound, curr_weight, level, path):


    for i in range(v):
        if (graph[path[level-1]][i] != 0 and
            not(i in path)):
            temp = curr_weight + graph[path[level - 1]][i]
            path[level] = i

            if (temp + (v - level + 1) * min_cost < curr_bound):
                curr_bound = min(curr_bound, tsp_bb(graph, v, curr_bound, temp, level + 1, path))
    if level == v:
        if graph[path[level - 1]][path[0]] != 0: #check if there is a path between level-1 and 1
            curr_bound= min(curr_bound, curr_weight + graph[path[level-1]][path[0]])
        else:
            return inf
    return curr_bound


TSP()
