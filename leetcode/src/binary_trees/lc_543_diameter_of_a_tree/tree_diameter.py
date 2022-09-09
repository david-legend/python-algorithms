class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def tree_diameter(root):
    def tree_diameter_helper(node):
        nonlocal diameter
        if node is None:
            return 0
        
        left = tree_diameter_helper(node.left)
        right = tree_diameter_helper(node.right)

        diameter = max(diameter, left + right)

        return max(left, right) + 1

    diameter = 0
    tree_diameter_helper(root)

    return diameter