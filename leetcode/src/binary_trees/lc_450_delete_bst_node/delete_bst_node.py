

# Solution 1 
# returns the inorder successor when the target node has both children
def delete_node(root, target):
    if root is None: return

    if root.val == target:
        if not root.left and not root.right:
            return None
        elif root.left and not root.right:
            return root.left
        elif not root.left and root.right:
            return root.right
        
        it = root.right
        while it.left:
            it = it.left
        root.val = it.val
        root.right = delete_node(root.right, it.val)
    elif target < root.val:
        root.left = delete_node(root.left, target)
    else:
        root.right = delete_node(root.right, target)
    
    return root



# Solution 2
# returns the inorder predecessor when the target node has both children
def delete_node_2(root, target):
    if root is None: return

    if root.val == target:
        if not root.left and not root.right:
            return None
        elif root.left and not root.right:
            return root.left
        elif not root.left and root.right:
            return root.right
        
        it = root.left
        while it.right:
            it = it.right
        root.val = it.val
        root.left = delete_node_2(root.left, it.val)
    elif target < root.val:
        root.left = delete_node_2(root.left, target)
    else:
        root.right = delete_node_2(root.right, target)
    
    return root