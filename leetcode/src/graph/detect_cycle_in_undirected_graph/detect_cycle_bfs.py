from collections import deque, namedtuple


# Time complexity for undirected graph O(V + 2E) + O(V)
# Where V is the number of vertices/nodes and E is the number of edges

# Space Complexity -> O(V) 
# Where V is the number of vertices/nodes

def is_cycle(v, neighbors):
    graph = {i: neighbors[i-1] for i in range(1, v)}
    visited = set()

    for i in range(1, v):
        if i not in visited:
            if detect_cycle(i, graph, visited): return True

    return False

def detect_cycle(node, graph, visited):
    Data = namedtuple('Data', ['node', 'parent'])
    queue = deque([Data(node, -1)])
    visited.add(node)

    while queue:
        node, parent = queue.popleft()

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(Data(neighbor, node))
            elif neighbor != parent:
                return True
    return False

neighbors_1 = [[2,3], [1,5], [1,4,6], [3], [2,7], [3,7], [5,6]]
neighbors_2 = [[2,3], [1,5], [1,4,6], [3], [2], [3]]


print(is_cycle(8, neighbors_1)) #True
print(is_cycle(7, neighbors_2)) #False