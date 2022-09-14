def sum_numbers(root):
    def sum_numbers_helper(node, curr_sum):
        if node is None: return 0

        curr_sum = curr_sum * 10 + node.val
        if node.left is None and node.right is None:
            return curr_sum

        return sum_numbers_helper(node.left, curr_sum) + sum_numbers_helper(node.right, curr_sum)

    return sum_numbers_helper(root, 0)