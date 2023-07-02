def get_strongly_connected_components(graph):
    stack, visited = [], [0] * len(graph)
    for i in range(len(graph)):
        if visited[i] == 0:
            top_sort(i , graph, stack, visited)
    
    transposed = transpose_graph(graph, visited)

    result = []
    while stack:
        node = stack.pop()
        if visited[node] == 0:
            components = []
            get_components(node, transposed, visited, components)
            result.append(components)

    return result

def top_sort(node, graph, stack, visited):
    visited[node] = 1
    for neighbor in graph[node]:
        if visited[neighbor] == 0:
            top_sort(neighbor, graph, stack, visited)
    stack.append(node)

def transpose_graph(graph, visited):
    transpose = [[] for _ in range(len(graph))]

    for i in range(len(graph)):
        visited[i] = 0
        for neighbor in graph[i]:
            transpose[neighbor].append(i)
    return transpose

def get_components(node, graph, visited, data):
    visited[node] = 1
    data.append(node)

    for neighbor in graph[node]:
        if visited[neighbor] == 0:
            get_components(neighbor, graph, visited, data)


data = [[1], [2, 3], [0], [4], []]
print(get_strongly_connected_components(data))