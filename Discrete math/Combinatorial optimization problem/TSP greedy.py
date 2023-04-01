def tsp_greedy(graph, start_node):
    n = len(graph)
    visited = [False] * n
    path = [start_node]
    visited[start_node] = True
    for _ in range(n-1):
        min_distance = float('inf')
        next_node = None
        for j in range(n):
            if not visited[j] and graph[path[-1]][j] < min_distance:
                min_distance = graph[path[-1]][j]
                next_node = j
        path.append(next_node)
        visited[next_node] = True
    path.append(start_node)
    return path

graph = [[0, 3, 14, 18,15], [3,0,4,22,20],
             [17, 9, 0, 16,4], [9, 20, 7, 0,18],[9,15,11,5,0]]
print(tsp_greedy(graph,0))