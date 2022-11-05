from collections import defaultdict

class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val

def calcEquation(equations, values, queries):
    graph = defaultdict(list)
    build_graph(graph, equations, values)

    result = []
    for query in queries:
        numerator, denominator = query
        if numerator not in graph or denominator not in graph:
            result.append(-1.0)
        else:
            ans = dfs(graph, set(), numerator, denominator)
            result.append(ans)
    
    return result

def build_graph(graph, equations, values):
    for i, equation in enumerate(equations):
        numerator, denominator = equation
        graph[numerator].append(Node(denominator, values[i]))
        graph[denominator].append(Node(numerator, 1/values[i]))

def dfs(graph, visited, src, dest):
    if src == dest: return 1.0
    visited.add(src)

    for node in graph[src]:
        if node.key not in visited:
            ans = dfs(graph, visited, node.key, dest)
            if ans != -1:
                return ans * node.val
    return -1

print(calcEquation([["a","b"],["b","c"],["bc","cd"]], [1.5,2.5,5.0], [["a","c"],["c","b"],["bc","cd"],["cd","bc"]])) #[3.75000,0.40000,5.00000,0.20000]

print(calcEquation([["a","b"]], [0.5], [["a","b"],["b","a"],["a","c"],["x","y"]])) #[0.5, 2.0, -1.0, -1.0]

print(calcEquation([["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]], [3.0,4.0,5.0,6.0], 
[["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]])) #[360.00000,0.00833,20.00000,1.00000,-1.00000,-1.00000]