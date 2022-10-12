def invert_binary_tree(root):
    def invert_tree_helper(node):
        if not node: return

        left = invert_tree_helper(node.left)
        right = invert_tree_helper(node.right)

        node.left, node.right = right, left
        return node

    return invert_tree_helper(root)