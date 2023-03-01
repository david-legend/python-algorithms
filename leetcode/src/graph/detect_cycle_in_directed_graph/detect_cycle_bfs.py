from collections import deque


# Find the topological ordering of the nodes, if the length of the ordering is equal to the number of nodes
# Then there's no cycle, if the opposite is true then theres a cycle
def is_cycle(v, graph):
    indegrees = {i: 0 for i in range(v)}

    for node in range(v):
        neighbors = graph[node]
        for neighbor in neighbors:
            indegrees[neighbor] += 1

    sources = deque()
    for node in indegrees:
        if indegrees[node] == 0:
            sources.append(node)
    
    if len(sources) == 0: return True
    ordering = []
    while sources:
        curr_node = sources.popleft()
        ordering.append(ordering)
        for node in graph[curr_node]:
            indegrees[node] -= 1
            if indegrees[node] == 0:
                sources.append(node)

    return False if len(ordering) == v else True

neighbors = [[1], [2], [3,5], [4], [], [4], [1,7], [8], [6]]
data = [[1], [2], [3,5], [4], [], [4], [1,7], [8], []]

print(is_cycle(9, neighbors)) #True
print(is_cycle(9, data)) #False