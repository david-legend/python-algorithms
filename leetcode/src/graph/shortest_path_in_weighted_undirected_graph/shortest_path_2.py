from heapq import *

def shortest_path(graph, V, source):
    parent, distance = [-1] * V, [float('inf')] * V
    min_heap = [(0, source)]
    distance[source], parent[source] = 0, source

    while min_heap:
        parent_weight, node = heappop(min_heap)
        
        for neighbor in graph[node]:
            child_node, child_weight = neighbor
            computed_distance =  parent_weight + child_weight

            if computed_distance < distance[child_node]:
                distance[child_node] = computed_distance
                parent[child_node] = node

                heappush(min_heap, (computed_distance, child_node))
    
    idx = V-1
    if parent[idx] == float('inf'):
        return [-1]
    
    path = []
    while idx != 0:
        path.append(idx)
        idx = parent[idx]
    path.append(0)
    path.reverse()

    return path



graph = [
    [[1,2], [3, 1]],
    [[0,2], [2, 4], [4,5]],
    [[1,4], [3,3], [4, 1]],
    [[0,1], [2,3]],
    [[1,5], [2,1]]
]

print(shortest_path(graph, 5, 0))