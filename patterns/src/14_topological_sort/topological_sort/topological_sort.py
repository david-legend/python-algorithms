from collections import deque

# Time Complexity
# During the step where we loop through the sources and decrease the in_degrees of the children, 
# each vertex will become a source only once and each edge will be accessed and removed once. 
# Therefore, the time complexity of the above algorithm will be O(V+E), 
# where ‘V’ is the total number of vertices and ‘E’ is the total number of edges in the graph.

# Space Complexity
# The space complexity will be O(V+E), 
# since we are storing all of the edges for each vertex in an adjacency list.

def topological_sort(vertices, edges):
    sorted_order = []
    if vertices <= 0:
        return []
    # initialize graph
    in_degrees = {i : 0 for i in range(vertices)}
    graph = {i: [] for i in range(vertices)}
    
    # Build the graph
    for edge in edges:
        parent, child = edge[0], edge[1]
        graph[parent].append(child)
        in_degrees[child] += 1
        
    # Find all sources i.e., all vertices with 0 in-degrees
    sources = deque()
    for key in in_degrees:
        if in_degrees[key] == 0:
            sources.append(key)
    
   # For each source, add it to the sorted_order and subtract one from all of its children's in-degrees
   # if a child's in-degree becomes zero, add it to the sources queue
    while sources:
        vertex = sources.popleft()
        sorted_order.append(vertex)
        for child in graph[vertex]:
            in_degrees[child] -= 1
            if in_degrees[child] == 0:
                sources.append(child)
    
    # topological sort is not possible as the graph has a cycle      
    if len(sorted_order) != vertices:
        return []
    
    return sorted_order

def main():
    print("Topological sort: " +
        str(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]])))
    print("Topological sort: " +
        str(topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]])))
    print("Topological sort: " +
        str(topological_sort(7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]])))


main()
