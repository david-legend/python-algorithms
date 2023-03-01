def top_sort(v, graph):
    visited, ordering = set(), []
    for i in range(v):
        if i not in visited:
            dfs(i, graph, visited, ordering)
    
    ordering.reverse() # res = ordering[::-1] (we could also slice and return the result)
    return ordering

def dfs(node, graph, visited, ordering):
    visited.add(node)
    
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, graph, visited, ordering)
    ordering.append(node)

graph = [[], [], [3], [1], [0,1], [0,2]]
print(top_sort(6, graph))