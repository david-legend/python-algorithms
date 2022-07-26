class Node:
    def __init__(self, val) -> None:
        self.val, self.neighbors = val, []

def dfs(node, target):
    visited = set()
    def find_node(node, target):
        if node is None: return False
        if node.val == target: return True
            
        for neighbor in node.neighbors:
            if neighbor in visited: continue
            visited.add(neighbor)

            found = dfs(neighbor, target)
            if found: return True
        
        return False
    
    return find_node(node, target)

n1 = Node(2)
n2 = Node(14)
n3 = Node(4)
n4 = Node(16)
n5 = Node(19)
n6 = Node(42)
n7 = Node(21)

n1.neighbors = [n2]
n2.neighbors = [n3]
n3.neighbors = [n4]
n4.neighbors = [n5, n6]
n6.neighbors = [n7]

print(dfs(n1, 42)) # True
print(dfs(n1, 98)) # True