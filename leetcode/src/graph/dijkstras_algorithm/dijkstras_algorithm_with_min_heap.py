from heapq import *

def dijkstra(v, graph, source):
    min_heap = [(0, source)]
    distances = [float('inf') for _ in range(v)]
    distances[source] = 0

    while min_heap:
        parent_weight, parent = heappop(min_heap)
        for neighbor in graph[parent]:
            child, child_weight = neighbor
            computed_distance =  parent_weight + child_weight

            if computed_distance < distances[child]:
                distances[child] = computed_distance
                heappush(min_heap, (computed_distance, child))
    return distances



graph = [
    [[1,4], [2,4]], 
    [[0,4], [2,2]],
    [[0,4], [1,2], [3,3], [4,1], [5,6]],
    [[2,3], [5,2]],
    [[2,1], [5,3]],
    [[2,6], [3,2], [4,3]],
]
print(dijkstra(6, graph, 0))