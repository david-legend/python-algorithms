class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def longest_univalue_path(root):
    max_length = 0

    def longest_univalue_path_helper(node):
        nonlocal max_length

        if node is None:
            return 0
        
        left = longest_univalue_path_helper(node.left)
        if node.left and node.val == node.left.val:
            left += 1
        else:
            left = 0
        

        right = longest_univalue_path_helper(node.right)
        if node.right and node.val and node.right.val:
            right += 1
        else:
            right = 0
        
        max_length = max(max_length, left + right)
        
        return max(left, right)
    
    if root:
        longest_univalue_path_helper(root)
    
    return max_length