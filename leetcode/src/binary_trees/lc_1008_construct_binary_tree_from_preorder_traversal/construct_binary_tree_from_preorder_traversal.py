class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def bst_from_preorder(preorder):
    def bst_from_preorder_helper(lower_bound, upper_bound):
        nonlocal idx 
        if idx >= len(preorder): return

        node_val = preorder[idx]
        if not(lower_bound < node_val < upper_bound):
            return None
        
        idx += 1
        left = bst_from_preorder_helper(lower_bound, node_val)
        right = bst_from_preorder_helper(node_val, upper_bound)

        return TreeNode(node_val, left, right)
    
    idx = 0
    return bst_from_preorder_helper(float('-inf'), float('inf'))