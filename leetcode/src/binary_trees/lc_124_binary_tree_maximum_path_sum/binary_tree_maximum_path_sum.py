def maxPathSum(root):
    def maxPathSumHelper(node):
        nonlocal max_sum
        if node is None: return 0
        
        left = maxPathSumHelper(node.left)
        right = maxPathSumHelper(node.right)
        
        left_tree_sum = left + node.val
        right_tree_sum = right + node.val
        left_right_tree_sum = left + right + node.val
        max_sum = max(max_sum, node.val, left_tree_sum, right_tree_sum, left_right_tree_sum)
        
        
        return max(node.val, left_tree_sum, right_tree_sum)
    
    max_sum = float('-inf')
    maxPathSumHelper(root)
    
    return max_sum