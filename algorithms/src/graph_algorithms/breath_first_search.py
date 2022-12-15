from collections import deque

def bfs(graph, vertex):
    if vertex:
        result, visited = [], set(vertex)
        queue = deque([vertex])

        while queue:
            curr_node = queue.popleft()
            result.append(curr_node)

            for node in graph[curr_node]:
                if node not in visited:
                    queue.append(node)
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

print(bfs(graph, "a"))