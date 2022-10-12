def lca_bst(root, p, q):
    if not root: return
    if p.val < root.val and q.val < root.val:
        return lca_bst(root.left, p, q)
    elif p.val > root.val and q.val > root.val:
        return lca_bst(root.right, p, q)
    else:
        return root