from collections import defaultdict

class Graph(object):
    def __init__(self, num_of_vertices):
        self.graph = defaultdict(list)
            
    
    def add_edge(self, vertex, edge):
        self.graph[vertex].append(edge)
        
    def topological_sort_util(self, vertex, visited, stack):
        visited.append(vertex)       
        
        for v in self.graph[vertex]:
            if not v in visited:
                self.topological_sort_util(v, visited, stack)  
                
        stack.insert(0, vertex)
        
    def topological_sort(self):
        visited = []
        stack = []
        
        for vertex in list(self.graph):
            if vertex not in visited:
                visited.append(vertex)
                self.topological_sort_util(vertex, visited, stack)
        
        return stack 


graph = Graph(8)

graph.add_edge("A", "C")
graph.add_edge("C", "E")
graph.add_edge("E", "H")
graph.add_edge("E", "F")
graph.add_edge("F", "G")
graph.add_edge("B", "D")
graph.add_edge("B", "C")
graph.add_edge("D", "F")

print(graph.topological_sort())