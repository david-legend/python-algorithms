class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def find_leaves(root):
    all_leaf_nodes = []
    while root.left or root.right:
        leaf_nodes = []
        is_leaf_node(root, leaf_nodes)
        all_leaf_nodes.append(leaf_nodes)
    
    all_leaf_nodes.append([root.val])
    return all_leaf_nodes

def is_leaf_node(node, leaf_nodes):
    if not node:
        return False
    
    if not node.left and not node.right:
        return True
    
    if is_leaf_node(node.left, leaf_nodes):
        leaf_nodes.append(node.left.val)
        node.left = None
    
    if is_leaf_node(node.right, leaf_nodes):
        leaf_nodes.append(node.right.val)
        node.right = None
    
    return False

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Leaves of Tree: ", find_leaves(root))