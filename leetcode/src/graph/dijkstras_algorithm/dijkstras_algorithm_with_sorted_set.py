from sortedcontainers import SortedSet

def dijkstra(v, graph, source):
    sets = SortedSet()
    sets.add((0, source))
    distances = [float('inf') for _ in range(v)]
    distances[source] = 0

    while sets:
        parent_weight, parent = sets.pop(0)
        for neighbors in graph[parent]:
            neighbor, neighbor_weight = neighbors
            computed_distance = parent_weight + neighbor_weight

            if computed_distance < distances[neighbor]:
                if distances[neighbor] != float('inf'):
                    sets.remove((distances[neighbor], neighbor))
                distances[neighbor] = computed_distance
                sets.add((computed_distance, neighbor))

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