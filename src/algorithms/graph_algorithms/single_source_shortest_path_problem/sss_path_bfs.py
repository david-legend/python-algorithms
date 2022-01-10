#find single shortest path using BFS
#This doesn't work for weighted graphs (see dijkstras_algorithm_sssp.py)

class Graph(object):
    def __init__(self, data=None):
        if data is None:
            data = {}
        self.graph = data
        
    def add_edge(self, vertex, edge):
        self.graph[vertex].append(edge)
        
    def find_shortest_path(self, source, dest):
        queue = []
        queue.append([source])
        
        while queue:
            path = queue.pop(0)
            node = path[-1]
            
            if node == dest:
                return path
            
            for vertex in self.graph.get(node, []):
                new_path = list(path)
                new_path.append(vertex)
                queue.append(new_path)
                

sample_graph = {
    "a": ["b", "c"],
    "b": ["d", "g"],
    "c": ["d", "e"],
    "d": ["f"],
    "e": ["f"],
    "g": ["f"]
}

graph = Graph(sample_graph)

path = graph.find_shortest_path("a", "f")

print(path)