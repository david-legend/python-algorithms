def countNodes(root):
    def countNodesHelper(node):
        nonlocal count
        if node is None: return
        
        countNodesHelper(node.left)
        count += 1
        countNodesHelper(node.right)
    
    count = 0
    if root:
        countNodesHelper(root)
    
    return count