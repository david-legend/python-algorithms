def max_depth_of_tree(root):
    if not root: return 0

    left = max_depth_of_tree(root.left)
    right = max_depth_of_tree(root.right)

    return max(left, right) + 1