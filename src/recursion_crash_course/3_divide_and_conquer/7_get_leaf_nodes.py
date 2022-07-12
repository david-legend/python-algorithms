class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = self.right = None

def get_leaf_nodes(node):
    result = []

    def gather_leaves(node):
        if node is None:
            return
        
        if node.left is None and node.right is None:
            result.append(node.val)
        
        gather_leaves(node.left)
        gather_leaves(node.right)

    gather_leaves(node)
    return result


# Example
#         100
#         / \
#     70       120
#   /   \
#  50   80


root = Node(100)
root.left = Node(70)
root.right = Node(120)
root.left.left = Node(50)
root.left.right = Node(80)

print(get_leaf_nodes(root)) #[50, 80, 120]