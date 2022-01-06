class Graph(object):
    def __init__(self, graph=None):
        if not graph:
            self.adj_list = {}
        else:
            self.adj_list = graph
            
    
    def add(self, vertex, edge):
        self.adj_list[vertex].append(edge)
        
    def bfs(self, vertex):
        if vertex:
            visited = [vertex]
            queue = [vertex]
            
            while queue:
                curr_vertex = queue.pop(0)
                print(curr_vertex)
                for adj_vertex in self.adj_list[curr_vertex]:
                    if adj_vertex not in visited:
                        visited.append(adj_vertex)
                        queue.append(adj_vertex)
                        
    def dfs(self, vertex):
        if vertex:
            visited = [vertex]  
            stack = [vertex] 
            
            while stack:
                curr_vertex = stack.pop()
                print(curr_vertex)
                
                for adj_vertex in self.adj_list[curr_vertex]:
                    if adj_vertex not in visited:
                        visited.append(adj_vertex)
                        stack.append(adj_vertex)
                
                
             
            

sample = {
    "a": ["b", "c"],
    "b": ["a", "d", "e"],
    "c": ["a", "e"],
    "d": ["b", "e", "f"],
    "e": ["d", "f"],
    "f": ["d", "e"],
}

graph = Graph(sample)

graph.bfs("a")

print("\n\n")

graph.dfs("a")

