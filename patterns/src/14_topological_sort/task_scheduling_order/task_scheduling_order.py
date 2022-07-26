from collections import deque
# Time Complexity
# During the step where we loop through the sources and decrease the in_degrees of the children, 
# each vertex will become a source only once and each edge will be accessed and removed once. 
# Therefore, the time complexity of the above algorithm will be O(V+E), 
# where ‘V’ is the total number of vertices and ‘E’ is the total number of edges in the graph.

# Space Complexity
# The space complexity will be O(V+E), 
# since we are storing all of the edges for each vertex in an adjacency list.

def find_order(tasks, prerequisites):
    sorted_order = []
    if tasks <= 0:
        return []
    
    # initialize graph
    in_degrees = {i: 0 for i in range(tasks)}
    graph = {i: [] for i in range(tasks)}
    
    # build graph
    for prerequisite in prerequisites:
        parent, child = prerequisite[0], prerequisite[1]
        graph[parent].append(child)
        in_degrees[child] += 1
        
    # find sources
    sources = deque()
    for key in in_degrees:
        if in_degrees[key] == 0:
            sources.append(key)
    
    # decrease in_degrees of the children of current sources and add new sources
    while sources:
        vertex = sources.popleft()
        sorted_order.append(vertex)
        
        for adj_vertex in graph[vertex]:
            in_degrees[adj_vertex] -= 1
            if in_degrees[adj_vertex] == 0:
                sources.append(adj_vertex)
    
    if len(sorted_order) != tasks:
        return []
    
    return sorted_order


def main():
    print("Is scheduling possible: " + str(find_order(3, [[0, 1], [1, 2]])))
    print("Is scheduling possible: " +
        str(find_order(3, [[0, 1], [1, 2], [2, 0]])))
    print("Is scheduling possible: " +
        str(find_order(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])))


main()