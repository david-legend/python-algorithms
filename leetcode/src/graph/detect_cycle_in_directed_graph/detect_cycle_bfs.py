from collections import deque


# Find the topological ordering of the nodes, if the length of the ordering is equal to the number of nodes
# Then there's no cycle, if the opposite is true then theres a cycle
def is_cycle(v, adj):
    graph, indegrees = {}, {}
    for i in range(1, v+1):
        graph[i], indegrees[i] = [], 0

    for node in range(1, v+1):
        neighbors = adj[node-1]
        for neighbor in neighbors:
            graph[node].append(neighbor)
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

neighbors = [[2], [3], [4,6], [5], [], [5], [2,8], [9], [7]]
data = [[2], [3], [4,6], [5], [], [5], [2,8], [9], []]

print(is_cycle(9, neighbors)) #True
print(is_cycle(9, data)) #False