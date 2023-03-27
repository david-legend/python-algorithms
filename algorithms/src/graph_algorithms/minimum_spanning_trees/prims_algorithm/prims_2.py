from heapq import *

def prims_algo(n, graph, source):
    visited, min_spanning_tree = [-1] * n, []
    visited[source] = 1
    min_heap = [(0, source, -1)]
    mst_sum = 0
    while min_heap:
        weight, node, parent = heappop(min_heap)
        if parent != -1 and visited[node] == -1:
            visited[node] = 1
            min_spanning_tree.append([node, parent])
            mst_sum += weight                                                                                                                                                                                   

        for neighbor in graph[node]:
            _, child, child_weight = neighbor
            if visited[child] == -1:
                heappush(min_heap, (child_weight, child, node))
    
    
    return min_spanning_tree


graph = [
    [[0,1,2], [0,2,1]], 
    [[1,0,2], [1,2,1]],
    [[2,0,1], [2,1,1], [2,4,2], [2,3,2]], 
    [[3,2,2],[3,4,1]],
    [[4,3,1]]
]

# print(graph[0])
print(prims_algo(5, graph, 0))
