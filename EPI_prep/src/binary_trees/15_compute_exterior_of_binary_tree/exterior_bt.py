from logging import root


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Example 1
#          1
#      /       \
#     2         3
#    / \       / \
#   4   5     6   7

# Given example 1, the exteriors of this tree will be 
# 1. the root -->   [1]
# 2. all the boundaries on left subtree and leaves [2, 4, 5]
# 3. all the boundaries on right subtree and leaves [3, 6, 7]
# We want the final result in this order
#            root
#            /   \
#           /     \
#          /_ _ _ _\
# root, left subtree boundaries, left subtree leaves, right subtree leaves, right subtree boundaries
# hence = [1, 2, 4, 5, 6, 7, 3]

# Example 2
#           1
#      /        \
#     2           3
#    /   \       / \
#   4     5     6   7
#    \   /         / \
#    9  11        13 21

# Given example 2, the exteriors of this tree will be 
# 1. the root -->   [1]
# 2. all the boundaries on left subtree and leaves [2, 4, 9, 11]
# 3. all the boundaries on right subtree and leaves [3, 6, 7, 13, 21]
# final result = [1, 2, 4, 9, 11, 6, 13, 21, 7, 3]

# Solution 
# 1. Make a preorder traversal on the left subtree to collect the boundaries on left subtree and leaves
# 2. Make a postorder traversal on the right subtree to collect the boundaries on right subtree and leaves

# Breakdown
# During these traversal we carefully compute what is a boundary and what is a leaf
# To compute a leaf we check if the node has no children

# To check if a node is a boundary in the left subtree
#   ---> we check if the current nodes parent has a left child, if it doesn't, then it is a boundary

# To check if a node is a boundary in the right subtree
#   ---> we check if the current nodes parent has a right child, if it doesn't, then it is a boundary

def exterior_binary_tree(tree):
    if tree:
        left_boundary_result = left_boundary_and_leaves(tree.left, True)
        right_boundary_result = right_boundary_and_leaves(tree.right, True)
        return [tree.val] + left_boundary_result + right_boundary_result
    else:
        return []

def is_leaf(node):
    if node:
        if node.left is None and node.right is None:
            return True
    return False

def left_boundary_and_leaves(subtree, is_boundary):
    if not subtree:
        return []

    data = [subtree.val]  if is_boundary or is_leaf(subtree) else []
    left_result = left_boundary_and_leaves(subtree.left, is_boundary)
    right_result = left_boundary_and_leaves(subtree.right, is_boundary and not subtree.left)

    return data + left_result + right_result

def right_boundary_and_leaves(subtree, is_boundary):
    if not subtree:
        return []

    left_result = right_boundary_and_leaves(subtree.left, is_boundary and not subtree.right)
    right_result = right_boundary_and_leaves(subtree.right, is_boundary)
    data = [subtree.val]  if is_boundary or is_leaf(subtree) else []

    return left_result + right_result + data

node_1 = TreeNode(1)
node_2 = TreeNode(2)
node_3 = TreeNode(3)
node_4 = TreeNode(4)
node_5 = TreeNode(5)
node_6 = TreeNode(6)
node_7 = TreeNode(7)

node_1.left, node_1.right = node_2, node_3
node_2.left, node_2.right = node_4, node_5
node_3.left, node_3.right = node_6, node_7

#         1
#      /       \
#     2         3
#    / \       / \
#   4   5     6   7
# print(exterior_binary_tree(node_1)) #[1, 2, 4, 5, 6, 7, 3]

node_4.right, node_5.left = TreeNode(9), TreeNode(11)
node_7.left, node_7.right = TreeNode(13), TreeNode(21)

#           1
#      /        \
#     2           3
#    /   \       / \
#   4     5     6   7
#    \   /         / \
#    9  11        13 21
print(exterior_binary_tree(node_1)) #[1, 2, 4, 9, 11, 6, 13, 21, 7, 3]