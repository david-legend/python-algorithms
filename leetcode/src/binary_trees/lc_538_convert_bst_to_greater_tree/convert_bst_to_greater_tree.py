def convertBST(root):
    def convertBstHelper(node):
        nonlocal running_sum
        if node is None: return
        
        convertBstHelper(node.right)
        
        node.val += running_sum
        running_sum = node.val
        
        convertBstHelper(node.left)
        
    running_sum = 0
    convertBstHelper(root)
    return root