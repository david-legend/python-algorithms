from collections import deque

def top_sort(v, graph):
    indegrees = {i: 0 for i in range(v)}

    for node in range(v):
        neighbors = graph[node]
        for neighbor in neighbors:
            indegrees[neighbor] += 1

    sources = deque()
    for node in indegrees:
        if indegrees[node] == 0:
            sources.append(node)
    
    ordering = []
    while sources:
        curr_node = sources.popleft()
        ordering.append(curr_node)
        for node in graph[curr_node]:
            indegrees[node] -= 1
            if indegrees[node] == 0:
                sources.append(node)

    return ordering if len(ordering) == v else []

graph = [[], [], [3], [1], [0,1], [0,2]]
print(top_sort(6, graph))