class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Time O(m + h) where m is the number of keys in the interval and h is the height of the tree
# Space O (h)
def range_lookup(tree, interval):
    start, end = interval[0], interval[1]
    result = []
    def range_lookup_helper(node):
        if node is None:
            return

        if start <= node.val <= end:
            range_lookup_helper(node.left)
            result.append(node.val)
            range_lookup_helper(node.right)
        elif node.val > end:
            range_lookup_helper(node.left)
        else:
            range_lookup_helper(node.right)
    
    range_lookup_helper(tree)
    return result

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
bst_9.left = bst_12
bst_4.right = bst_9

# Right Subtree
bst_2.left, bst_2.right = bst_5, bst_6
bst_5.right = bst_10
bst_10.left, bst_10.right = bst_13, bst_14
bst_13.right = bst_15
bst_6.right = bst_11

print(range_lookup(bst, [16, 31])) #[17, 19, 23, 29, 31]
print(range_lookup(bst, [31, 53])) #[31, 37, 41, 43, 47, 53]
print(range_lookup(bst, [2, 5])) #[2, 3, 5]
print(range_lookup(bst, [19, 29])) #[19, 23, 29]