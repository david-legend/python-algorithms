
def dfs(graph, vertex):
    if vertex:
        result, visited, stack = [], set(vertex), [vertex]

        while stack:
            curr_node = stack.pop()
            result.append(curr_node)

            for node in graph[curr_node]:
                if node not in visited:
                    stack.append(node)
                    visited.add(node)

        return result
        
graph = {
    "a": ["b", "c"],
    "b": ["a", "d", "e"],
    "c": ["a", "e"],
    "d": ["b", "e", "f"],
    "e": ["d", "f"],
    "f": ["d", "e"],
}

print(dfs(graph, "a"))