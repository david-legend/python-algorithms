class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def lca_bst(root, p, q):
    def lca_helper(node):
        if node is None:
            return None

        if p.val < node.val and q.val < node.val:
            return lca_bst(node.left, p, q)
        elif p.val > node.val and q.val > node.val:
            return lca_bst(node.right, p, q)
        else:
            return node
    
    return lca_helper(root)