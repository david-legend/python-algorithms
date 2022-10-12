def same_tree(p, q):
    if not p and not q: return True

    if p and q and p.val == q.val:
        return (same_tree(p.left, q.left) and 
                same_tree(p.right, q.right))
                
    return False