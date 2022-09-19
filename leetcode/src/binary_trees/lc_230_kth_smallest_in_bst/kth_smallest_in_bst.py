def kthSmallest(root, k):
    def kthSmallestBstHelper(node):
        nonlocal kth_smallest, count, found
        if node is None: return
        if found: return
        
        kthSmallestBstHelper(node.left)
        
        count += 1
        if count == k:
            kth_smallest, found = node.val, True
            return
            
        kthSmallestBstHelper(node.right)
    
    kth_smallest, count, found = None, 0, False
    kthSmallestBstHelper(root)
    return kth_smallest