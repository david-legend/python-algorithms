def min_diff_in_bst(root):
    def min_diff_in_bst_helper(node):
        nonlocal min_distance, prev_val
        if node is None: return

        min_diff_in_bst_helper(node.left)
        
        if prev_val != float('inf'):
            min_distance = min(min_distance, node.val - prev_val)
        prev_val = node.val

        min_diff_in_bst_helper(node.right)

    min_distance = prev_val = float('inf')
    min_diff_in_bst_helper(root)

    return min_distance