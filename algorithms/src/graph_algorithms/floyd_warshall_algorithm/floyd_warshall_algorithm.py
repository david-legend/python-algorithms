# Time O(N^3)
def floyd_warshall(graph):
    n = len(graph)
    for i in range(n):
        for j in range(n):
            if graph[i][j] == -1:
                graph[i][j] = float('inf')
            if i == j: graph[i][j] = 0
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    
    for i in range(n):
        for j in range(n):
            if graph[i][j] == float('inf'):
                graph[i][j] = -1

    return graph

data = [[0,1,43],[1,0,6],[-1,-1,0]]


print(floyd_warshall(data)) #[[0,1,7],[1,0,6],[-1,-1,0]]
