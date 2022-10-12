def subtree_of_another_tree(root, subroot):
    if not subroot: return True
    if not root: return False

    if same_tree(root, subroot):
        return True

    return (subtree_of_another_tree(root.left, subroot) or
            subtree_of_another_tree(root.right, subroot))


def same_tree(p, q):
    if not p and not q: return True

    if p and q and p.val == q.val:
        return (same_tree(p.left, p.left) and 
                same_tree(p.right, q.right))
    return False