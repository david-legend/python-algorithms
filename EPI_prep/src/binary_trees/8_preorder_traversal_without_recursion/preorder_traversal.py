class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

# Time: O(n)
# Space: O(h) - best case
# Space: O(n) - worst case - skewed tree


def preorder_traversal(tree):
    path, result = [], []

    while tree or path:
        if tree:
            result.append(tree.val)
            path.append(tree)
            tree = tree.left
        else:
            tree = path.pop()
            tree = tree.right
    
    return result

node_1 = Node(1)
node_2 = Node(2)
node_3 = Node(3)
node_4 = Node(4)
node_5 = Node(5)
node_6 = Node(6)
node_7 = Node(7)

node_1.left, node_1.right = node_2, node_3
node_2.left, node_2.right = node_4, node_5
node_3.left, node_3.right = node_6, node_7

print(preorder_traversal(node_1)) # [1, 2, 4, 5, 3, 6, 7]