from collections import deque
def findMinHeightTrees(n, edges):
    if n == 1:
        return [0]
    
    graph = {i: [] for i in range(n)}
    indegree = {i: 0 for i in range(n)}
    
    for edge in edges:
        n1, n2 = edge[0], edge[1]
        
        graph[n1].append(n2)
        graph[n2].append(n1)
        
        indegree[n1] += 1
        indegree[n2] += 1
    
    leaves = deque()
    for node in indegree:
        if indegree[node] == 1:
            leaves.append(node)
    
    total_nodes = n
    while total_nodes > 2:
        level_size = len(leaves)
        total_nodes -= level_size
        
        for _ in range(level_size):
            vertex = leaves.popleft()
            for node in graph[vertex]:
                indegree[node] -= 1
                if indegree[node] == 1:
                    leaves.append(node)
    
    return list(leaves)


print(findMinHeightTrees(4, [[1,0],[1,2],[1,3]])) #[1]
print(findMinHeightTrees(6, [[3,0],[3,1],[3,2],[3,4],[5,4]])) #[3, 4]
print(findMinHeightTrees(1, []))  #[0]