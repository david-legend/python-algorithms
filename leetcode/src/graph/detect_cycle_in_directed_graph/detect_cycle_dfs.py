def is_cycle(v, adj):
    visited, dfs_visited = [False] * (v+1), [False] * (v+1)
    graph = {i: adj[i-1] for i in range(v+1)}
    
    for i in range(1, v+1):
        if not visited[i]:
            if dfs(i, graph, visited, dfs_visited): return True
    
    return False

def dfs(node, graph, visited, dfs_visited):
    visited[node] = True
    dfs_visited[node] = True

    for neighbor in graph[node]:
        if not visited[neighbor]:
            if dfs(neighbor, graph, visited, dfs_visited): return True
        elif dfs_visited[neighbor]:
            return True
    
    dfs_visited[node] = False
    return False




neighbors = [[2], [3], [4,6], [5], [], [5], [2,8], [9], [7]]
data = [[2], [3], [4,6], [5], [], [5], [2,8], [9], []]

print(is_cycle(9, neighbors)) #True
print(is_cycle(9, data)) #False