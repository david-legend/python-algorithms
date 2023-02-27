from collections import deque
class Graph(object):
    def __init__(self, graph=None):
        self.adj_list = {} if graph is None else graph
            
    
    def add(self, node, edge):
        self.adj_list[node].append(edge)
        
    def bfs(self, node):
        if not node: return []

        visited = set(node)
        queue, result = deque([node]), []
        
        while queue:
            curr_node = queue.popleft()
            result.append(curr_node)
            for adj_node in self.adj_list[curr_node]:
                if adj_node not in visited:
                    visited.add(adj_node)
                    queue.append(adj_node)
        return result


    def dfs(self, node):
        if not node: return []
        def dfs_helper(node, graph, visited, result):
            visited.add(node)
            result.append(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs_helper(neighbor, graph, visited, result)

        visited, result = set(), []
        dfs_helper(node, self.adj_list, visited, result)
        return result

                
                
             
            

sample = {
    "a": ["b", "c"],
    "b": ["a", "d", "e"],
    "c": ["a", "e"],
    "d": ["b", "e", "f"],
    "e": ["d", "f"],
    "f": ["d", "e"],
}

graph = Graph(sample)

print(graph.bfs("a"))

print("\n\n")

print(graph.dfs("a"))

