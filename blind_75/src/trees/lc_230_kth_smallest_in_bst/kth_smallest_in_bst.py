def kth_smallest_in_bst(root, k):
    def kth_smallest_helper(node):
        nonlocal i, kth_smallest, found
        if not node: return 
        if found: return
        
        kth_smallest_helper(node.left)
        i += 1

        if i == k:
            kth_smallest, found = node.val, True
            return True

        kth_smallest_helper(node.right)

    i, kth_smallest, found = 0, None, False
    kth_smallest_helper(root)

    return kth_smallest