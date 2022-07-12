class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = self.right = None


def pre_order(node):
    if node is None:
        return

    print(node.val)
    pre_order(node.left)
    pre_order(node.right)

#         100
#         / \
#     70       120
#   /   \
#  50   80
def insert(node, val):
    if node is None:
        new_node = Node(val)
        return new_node
    
    if val <= node.val:
        node.left = insert(node.left, val)
    else:
        node.right = insert(node.right, val)
    
    return node

root = Node(100)
root.left = Node(70)
root.right = Node(120)
root.left.left = Node(50)
root.left.right = Node(80)


pre_order(insert(root, 60))