class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time O(n) | Space O(n) - Worst Case
# Time O(n) | Space O(h) - Best Case
def binary_tree_paths(root):
    def binary_tree_paths_helper(node, path):
        if node is None:
            return
        
        path.append(str(node.val))
        if node.left is None and node.right is None:
            result.append("->".join(path))
        else:
            binary_tree_paths_helper(node.left, path)
            binary_tree_paths_helper(node.right, path)
        
        path.pop()

    result = []
    binary_tree_paths_helper(root, [])
    return result