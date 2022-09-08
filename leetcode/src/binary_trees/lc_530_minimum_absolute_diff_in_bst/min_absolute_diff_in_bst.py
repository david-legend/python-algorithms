class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def min_absolute_diff(root):
    min_diff = prev_val = float('inf')
    def min_absolute_diff_helper(node):
        nonlocal min_diff, prev_val
        if node is None:
            return
        
        min_absolute_diff_helper(node.left)

        if prev_val != float('inf'):
            min_diff = min(min_diff, abs(node.val - prev_val))
        
        prev_val = node.val
        min_absolute_diff_helper(node.right)
        
    min_absolute_diff_helper(root)
    return min_diff

