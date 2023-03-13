from heapq import *

# Time  - O(E log V) 
# where E is the total number of edges and V is the total number of nodes

# Space - O(V^2)  
# where V is the total number of nodes 
# (Note: considering a dense graph where each node is connected to each other, the min heap will at some point contain nodes more than V which can be approximated to V^2)

# Deriving Time Complexity
# O(V) -> while loop
# O(log V) -> pop from min heap
# O(V-1) -> looping through adjacent nodes
# O(log v) -> pushing to min heap

# O( V (log(heap size) + (V-1) (log heap size))))  -> factor log(heapsize) out
# O( V (log(heap size) (V- 1 + 1)) 
# O( V (log(heap size) * V) -> factor V out 
# O( V^2 (log(heap size))  
# What is heapsize -> considering a dense graph where each node is connected to each other, the min heap will at some point contain nodes more than V
# We can say heapsize is V2

# O( V^2 (log(V^2))  
# we can also say that log(V^2) is the same as 2logV
# Hence O(V^2 * 2 log V)
# We can also say that V^2 is equal to the number of edges since every node has a (V-1) edges in a highly dense graph, making it approximately V^2
# Hence -> O(2E log V) which can be simplified to O(E logV)

# Finally Time Complexity ->>  O(E log(V))

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