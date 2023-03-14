from heapq import *

# Time Complexity: O(m * log(n))
# Space Complexity: O(n)

def shortest_path(n, m, edges):
    graph = [[] for _ in range(n)]
    for i in range(m):
        node1, node2, weight = edges[i]
        graph[node1].append([node2, weight])
        graph[node2].append([node1, weight])

    parent, distance = [0] * n, [float('inf')] * n
    parent[0], distance[0] = 0, 0
    min_heap = [(0, 0)]

    while min_heap:
        parent_weight, node = heappop(min_heap)

        for neighbor in graph[node]:
            child, child_weight = neighbor
            computed_distance = child_weight + parent_weight

            if computed_distance < distance[child]:
                distance[child] = computed_distance
                parent[child] = node

                heappush(min_heap, (computed_distance, child))

    idx = n-1
    if distance[idx] == float('inf'):
        return [-1]

    path = []
    while idx != 0:
        path.append(idx)
        idx = parent[idx]
    path.append(0)
    path.reverse()

    return path

edges = [[0,1,2], [1,4,5], [1,2,4], [0,3,1], [3,2,3],[2,4,1]]
print(shortest_path(5, 6, edges))