def max_path_sum(root):
    def max_path_helper(node):
        nonlocal max_sum
        if not node: return 0

        left = max_path_helper(node.left)
        right = max_path_helper(node.right)

        left_sum, right_sum = node.val + left, node.val + right
        left_root_right_sum = left.val + node.val + right.val
        max_sum = max(max_sum, left_sum, right_sum, left_root_right_sum)

        return max(node.val, left_sum, right_sum)

    max_sum = float('-inf')
    max_path_helper(root)

    return max_sum