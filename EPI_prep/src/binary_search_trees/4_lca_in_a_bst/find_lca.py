class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_lca(tree, p, q):
    while tree:
        if p.val < tree.val and q.val < tree.val:
            tree = tree.left
        elif p.val > tree.val and q.val > tree.val:
            tree = tree.right
        else:
            return tree

    return None

def find_lca_recursive(tree, p, q):
    def find_lca_helper(node):
        if node is None:
            return None
        
        if p.val < node.val and q.val < node.val:
            return find_lca_helper(node.left)
        elif p.val > node.val and q.val > node.val:
            return find_lca_helper(node.right)
        else:
            return node
    
    return find_lca_helper(tree)

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


print("Iterative Solution\n")
print(find_lca(bst, bst_15, bst_5).val) 
print(find_lca(bst, bst_14, bst_15).val) 
print(find_lca(bst, bst_4, bst_9).val) 

print("\nRecursive Solution\n")
print(find_lca_recursive(bst, bst_15, bst_5).val) 
print(find_lca_recursive(bst, bst_14, bst_15).val) 
print(find_lca_recursive(bst, bst_4, bst_9).val) 
