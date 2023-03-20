from heapq import *

def prims_algo(n, graph, source):
    visited = [-1] * n
    min_heap = [(0, source)]
    mst_sum = 0
    while min_heap:
        weight, node = heappop(min_heap)
        if visited[node] == 1: continue
        visited[node] = 1
        mst_sum += weight
        for neighbor in graph[node]:
            _, child, child_weight = neighbor
            if visited[child] == -1:
                heappush(min_heap, (child_weight, child))
    
    return mst_sum


graph = [
    [[0,1,2], [0,2,1]], 
    [[1,0,2], [1,2,1]],
    [[2,0,1], [2,1,1], [2,4,2], [2,3,2]], 
    [[3,2,2],[3,4,1]],
    [[4,3,1]]
]

# print(graph[0])
print(prims_algo(5, graph, 0))
