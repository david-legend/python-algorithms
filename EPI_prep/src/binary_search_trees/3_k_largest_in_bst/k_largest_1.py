from collections import deque

# Time O(h + k) | Space O(h)

class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# This approach begins with the desired nodes, and work backwards. 
# We do this by recursing first on the right subtree and then on the left subtree. 
# This amounts to a reverse- inorder traversal

def find_k_largest(tree, k):
    k_largest_elements = []
    def find_k_largest_helper(node):
        if node and len(k_largest_elements) < k:
            find_k_largest_helper(node.right)

            if len(k_largest_elements) < k:
                k_largest_elements.append(node.val)
                find_k_largest_helper(node.left)
    
    find_k_largest_helper(tree)
    
    return k_largest_elements

    

bst = TreeNode(19)
bst_1 = TreeNode(7)
bst_2 = TreeNode(43)
bst_3 = TreeNode(3)
bst_4 = TreeNode(11)
bst_5 = TreeNode(23)
bst_6 = TreeNode(47)
bst_7 = TreeNode(2)
bst_8 = TreeNode(5)
bst_9 = TreeNode(17)
bst_10 = TreeNode(37)
bst_11 = TreeNode(53)
bst_12 = TreeNode(13)
bst_13 = TreeNode(29)
bst_14 = TreeNode(41)
bst_15 = TreeNode(31)

bst.left, bst.right = bst_1, bst_2
# Left Subtree
bst_1.left, bst_1.right = bst_3, bst_4
bst_3.left, bst_3.right = bst_7, bst_8
bst_9.left, bst_4.right = bst_12, bst_9

# Right Subtree
bst_2.left, bst_2.right = bst_5, bst_6
bst_5.right = bst_10
bst_10.left, bst_10.right = bst_13, bst_14
bst_13.right = bst_15
bst_6.right = bst_11


print(find_k_largest(bst, 3)) # [53, 47, 43]
print(find_k_largest(bst, 2)) # [53, 47]
print(find_k_largest(bst, 1)) # [53]
