# Best Case: Time O(n) | Space O(h)
# 
# Worst Case: Time O(n) | Space O(n)
class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_first_greater_than_than_k(tree, k):
    subtree, first_so_far = tree, None
    while subtree:
        if subtree.val > k:
            first_so_far, subtree = subtree, subtree.left
        else:
            subtree = subtree.right

    return first_so_far


    

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


print(find_first_greater_than_than_k(bst, 2).val) # 3
print(find_first_greater_than_than_k(bst, 23).val) # 29
print(find_first_greater_than_than_k(bst, 53)) # None
