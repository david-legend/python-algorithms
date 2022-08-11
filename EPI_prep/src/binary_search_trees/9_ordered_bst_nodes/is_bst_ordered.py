class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# A brute-force approach would be to check if the first node is a proper ancestor of the middle 
# and the second node is a proper descendant of the middle. If this check returns true, we return true.
# Otherwise, we return the result of the same check, swapping the roles of the first and second nodes

# Searching has time complexity O(h),where h is the height of the tree, since we can use the BST ProPerty 
# to prune one of the two children at each node. Since we perform a maximum of three searches, the total time complexity is O(h).
# The 3 searches being -> 
# 1. from first node to the midlle one
# 2. from second node to the middle one
# 3. from middle node to either one of them

# One disadvantage of trying the two input nodes for being the middle's ancestor one after another is that 
# we will waste one search, hence we will incur an O(h) time complexity esp when the nodes are closer to the middle

# We can prevent this by performing the searches for the middle from both altematives in an interleaved fashion. 
# If we encounter the middle from one node, we subsequently search for the second node from the middle. 
# This way we avoid performing an unsuccessful search on a large subtree

def is_bst_ordered(node0, node1, middle):
    search0, search1 = node0, node1

    # Perform interleaved searching from node0 and
    # node1 for middle.
    while search0 is not search1 and search0 is not middle \
        and search1 is not search0 and search1 is not middle \
        and (search0 or search1):

        if search0:
            search0 = search0.left if search0.val > middle.val else search0.right
        
        if search1:
            search1 = search1.left if search1.val > middle.val else search1.right
    
    # If both searches were unsuccessful , or we got fron
    # node0 to node1 without seeing middle, 
    # or from node1 to node0 without seeing middle, 
    # middle cannot lie between node0 and node1
    if (search0 is not middle and search1 is not middle) or \
        (search0 is search1 or search1 is search0):
        return False
    

    # If we get here, we already know one of node0 or node1 has a path to middle. 
    # Check if middle has a path node0 or to node1.
    return search(middle, node0 if search1 is middle else node1)

def search(source, target):
    while source and source is not target:
        source = source.left if source.val > target.val else source.right
    return source is target

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

print(is_bst_ordered(bst, bst_8, bst_3)) #True
print(is_bst_ordered(bst_7, bst_8, bst_12)) #False
print(is_bst_ordered(bst, bst_9, bst_1)) #True
print(is_bst_ordered(bst_1, bst_12, bst_9)) #True