from collections import defaultdict

def dfs(graph, v, visited):
    visited[v] = True
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

def is_strongly_connected(graph):
    n = len(graph)
    visited = [False] * n

    # Start DFS from the first vertex
    dfs(graph, 0, visited)

    # If all vertices are not visited, the graph is not strongly connected
    if not all(visited):
        return False

    # Create a transposed graph by reversing all edges
    transposed_graph = defaultdict(list)
    for v in range(n):
        for neighbor in graph[v]:
            transposed_graph[neighbor].append(v)

    # Reset the visited list and start DFS from the last vertex visited
    visited = [False] * n
    last_visited = 0
    for v, is_visited in enumerate(visited):
        if is_visited:
            last_visited = v
    dfs(transposed_graph, last_visited, visited)

    # If all vertices are visited, the graph is strongly connected, otherwise it is not
    return all(visited)
