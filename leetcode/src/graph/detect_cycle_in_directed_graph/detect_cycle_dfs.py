def is_cycle(v, graph):
    visited, dfs_visited = [False] * (v+1), [False] * (v+1)
    
    for i in range(v):
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




neighbors = [[1], [2], [3,5], [4], [], [4], [1,7], [8], [6]]
data = [[1], [2], [3,5], [4], [], [4], [1,7], [8], []]

print(is_cycle(9, neighbors)) #True
print(is_cycle(9, data)) #False