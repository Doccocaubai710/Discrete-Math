from math import inf
v = 5
graph = [[0, 3, 14, 18,15], [3,0,4,22,20],
             [17, 9, 0, 16,4], [9, 20, 7, 0,18],[9,15,11,5,0]]

path = [0] * (v+1)

min_cost=inf
for i in range(v):
    for j in range(v):
        if graph[i][j]<min_cost and graph[i][j]>0:
            min_cost=graph[i][j]
predict = [0] * 5
record = inf
cost = [0] * 5
def Try(k):
    global predict
    global record
    global cost
    for i in range (1, 5):
        if predict[k] <= record and i not in path:
            path[k] = i
            cost[k] = cost[k-1] + graph[path[k-1]][i]
            predict[k] = cost[k] + (v-k)*min_cost    
            if k == 4:
                path[k] = i
                record = cost[k] + graph[i][0]
                print(path)
                print(record)
            else:
                Try(k+1)
            

Try(1)