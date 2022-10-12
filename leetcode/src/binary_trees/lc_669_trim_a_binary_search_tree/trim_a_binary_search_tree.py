def trimBST(root, low, high):
    def trim(node):
        if not node: 
            return None
        elif node.val > high:
            return trim(node.left)
        elif node.val < low:
            return trim(node.right)
        else:
            node.left = trim(node.left)
            node.right = trim(node.right)
        
        return node

    return trim(root)