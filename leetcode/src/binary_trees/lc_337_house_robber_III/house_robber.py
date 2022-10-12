def rob(root):
    def robHelper(node):
        if not node: return [0,0]
        
        left = robHelper(node.left)
        right = robHelper(node.right)
        
        with_root = node.val + left[1] + right[1]
        without_root = max(left) + max(right)
        
        return [with_root, without_root]
    
    return max(robHelper(root))