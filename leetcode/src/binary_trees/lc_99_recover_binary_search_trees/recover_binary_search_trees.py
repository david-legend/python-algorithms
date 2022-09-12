def recover_bst(root):
    def recover_bst_helper(node):
        nonlocal prev, first, middle, last
        if not node: return

        recover_bst_helper(node.left)
        if prev and prev.val > node.val:
            if not first:
                first, middle = prev, node
            else:
                last = node

        prev = node
        recover_bst_helper(node.right)

    prev = first = middle = last = None
    recover_bst_helper(root)

    if first and last:
        first.val, last.val = last.val, first.val
    elif first and middle:
        first.val, middle.val = middle.val, first.val