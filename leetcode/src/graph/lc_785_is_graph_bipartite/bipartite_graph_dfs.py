from collections import deque

def isBipartite(graph) -> bool:
    color = [-1] * len(graph)

    for i in range(len(graph)):
        if color[i] == -1:
            if dfs(i, graph, color) == False: return False         
    return True
    
def dfs(node, graph, color):
    if color[node] == -1:
        color[node] = 0

    for neighbor in graph[node]:
        if color[neighbor] > -1:
            if color[neighbor] == color[node]: return False
        else:
            color[neighbor] = not color[node]
            if dfs(neighbor, graph, color) == False:
                return False
            
    return True

print(isBipartite([[1,2,3],[0,2],[0,1,3],[0,2]])) # False
print(isBipartite([[1,3],[0,2],[1,3],[0,2]])) # True
print(isBipartite([[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]])) # False