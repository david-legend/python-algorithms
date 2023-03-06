from collections import deque

def isBipartite( graph) -> bool:
    if len(graph) == 0: return True
    color = [-1] * len(graph)
    
    for i in range(len(graph)):
        if color[i] == -1:
            if not bfs(i, graph, color):
                return False
    return True
    
def bfs(node, graph, color):
    queue = deque([node])
    color[node] = 0

    while queue:
        curr_node = queue.popleft()
        for neighbor in graph[curr_node]:
            if color[neighbor] > -1:
                if color[neighbor] == color[curr_node]: return False
            else:
                color[neighbor] = not color[curr_node]
                queue.append(neighbor)
    
    return True

print(isBipartite([[1,2,3],[0,2],[0,1,3],[0,2]])) # False
print(isBipartite([[1,3],[0,2],[1,3],[0,2]])) # True
print(isBipartite([[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]])) # False