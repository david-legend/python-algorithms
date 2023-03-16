
# Time - O(VE + V) -> O(VE)
# Space - O(V)
# Where V is the number of vertices and E is the number of edges

def bellmanFord(n, edges, source):
    distance = [float('inf')] * n
    distance[source] = 0

    for _ in range(n-1):
        for edge in edges:
            u, v, weight = edge
            computed_distance = distance[u] + weight
            if distance[u] != float('inf') and computed_distance < distance[v]:
                distance[v] = computed_distance
        
    # checking for negative cycles
    for edge in edges:
        u, v, weight = edge
        computed_distance = distance[u] + weight
        if distance[u] != float('inf') and computed_distance < distance[v]:
            return [-1]
    
    return distance

edges = [[3,2,6], [5,3,1], [0,1,5], [1,5,-3], [1,2,-2], [3,4,-2], [2,4,3]]
edges_with_cycle = [[0,1,-2], [1,2,-1], [2,0,2]]

print(bellmanFord(6, edges, 0))
print(bellmanFord(3, edges_with_cycle, 0))