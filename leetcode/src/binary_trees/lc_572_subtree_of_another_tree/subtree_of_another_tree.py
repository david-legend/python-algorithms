# Time O(mn)
def is_subtree(root, sub_root):
    if not sub_root: return True
    if not root: return False

    if is_same_tree(root, sub_root):
        return True

    return is_subtree(root.left, sub_root) or is_subtree(root.right, sub_root)

def is_same_tree(s, q):
    if not s and not q: return True
    if s and q and s.val == q.val:
        return (is_same_tree(s.left, q.left) and is_same_tree(s.right, q.right))
    
    return False