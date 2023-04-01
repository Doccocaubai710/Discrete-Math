def has_cycle(graph):
    visited=False*len(graph)
    enter_time=[-1]*len(graph)
    exit_time=[-1]*len(graph)

    def DFS(node,time):
        nonlocal visited,enter_time,exit_time
        visited[node]=True
        enter_time[node]=time
        for neighbor in graph[node]:
            if not visited[neighbor]:
                if DFS(neighbor,time+1):
                    return True
            elif exit_time[neighbor]==-1 or enter_time[neighbor]>enter_time[node]:
                return True
        exit_time[node]=time
        return False
    for i in range(len(graph)):
        if not visited[i]:
            if DFS(i, 0):
                return True
    return False