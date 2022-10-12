from collections import defaultdict
def distanceK(root, target, k):
    if not root: return
    graph = defaultdict(list)
    build_graph(root, graph)

    result, visited = [], set()
    if target in graph:
        bfs(graph, visited, target, 0, k, result)

    return result

def build_graph(node, graph):
    if node is None: return

    if node.left:
        graph[node].append(node.left)
        graph[node.left].append(node)
        build_graph(node.left, graph)
    
    if node.right:
        graph[node].append(node.right)
        graph[node.right].append(node)
        build_graph(node.right, graph)

def bfs(graph, visited, node, count, k, result):
    visited.add(node)
    if count == k:
        result.append(node.val)
        return
    
    for path in graph[node]:
        if not (path in visited):
            bfs(graph, visited, path, count+1, k, result)