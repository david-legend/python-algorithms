
def two_sum_bst(root, target):
    def two_sum_helper(node):
        if node is None:
            return False

        diff = target - node.val
        if diff in value_map:
            return True

        value_map[node.val] = diff

        left = two_sum_helper(node.left)
        if left:
            return left

        right = two_sum_helper(node.right)
        if right:
            return right

        return False


    value_map = {}
    return two_sum_helper(root)