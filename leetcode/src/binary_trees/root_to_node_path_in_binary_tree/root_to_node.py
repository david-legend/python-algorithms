
class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

def findPath(root, destination):

    def solvePath(node, path):
        if node is None: return False

        path.append(node.val)
        if node == destination:
            return True
        
        if solvePath(node.left, path):
            return True

        if solvePath(node.right, path):
            return True

        path.pop()
        return False

    path = []
    solvePath(root, path)

    return path


node_1 = Node(4)
node_2 = Node(-4)
node_3 = Node(-2)
node_4 = Node(7)
node_5 = Node(1)
node_6 = Node(6)

node_1.left, node_1.right = node_2, node_3
node_2.right = node_4
node_3.left = node_5
node_4.right = node_6


print(findPath(node_1, node_6))
print(findPath(node_1, node_1))
print(findPath(node_1, node_5))
print(findPath(node_1, node_4))