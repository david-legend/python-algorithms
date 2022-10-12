def valid_bst(root):
    def valid_bst_helper(node, lower_bound, upper_bound):
        if node is None: return True

        if not (lower_bound < node.val < upper_bound):
            return False
        
        return (valid_bst_helper(node.left, lower_bound, node.val) and 
             valid_bst_helper(node.right, node.val, upper_bound))

    return valid_bst_helper(root, float('-inf'), float('inf'))