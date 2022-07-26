
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def root_to_leaf(root):
    all_paths = []
    get_paths(root, [], all_paths)
    
    return all_paths

def get_paths(root, current_path, all_paths):
    if root is None:
        return
    
    current_path.append(root.val)
    
    if root.left is None and root.right is None:
        all_paths.append(list(current_path))
    else:
        get_paths(root.left, current_path, all_paths)
        get_paths(root.right, current_path, all_paths)
    
    del current_path[-1]

root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(4)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)

print("All Root to Leaf paths in Tree " +
    ": " + str(root_to_leaf(root)))


