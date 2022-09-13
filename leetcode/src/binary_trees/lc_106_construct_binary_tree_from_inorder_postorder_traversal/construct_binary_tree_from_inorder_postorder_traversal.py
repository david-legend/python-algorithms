class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(inorder, postorder):
    inorder_values_to_index = {data: i for i, data in enumerate(inorder)}
    def buildTreeHelper(postorder_start, postorder_end, inorder_start, inorder_end):
        if postorder_start > postorder_end or inorder_start > inorder_end:
            return
        
        node_val = postorder[postorder_end]
        root_idx = inorder_values_to_index[node_val]
        subtree_size = root_idx - inorder_start
        
        left = buildTreeHelper(postorder_start, postorder_start + subtree_size - 1, 
                                inorder_start, root_idx -1)
        
        right = buildTreeHelper(postorder_start + subtree_size, postorder_end - 1, 
                                root_idx + 1, inorder_end)
        
        return TreeNode(node_val, left, right)
    
    return buildTreeHelper(0, len(postorder) - 1, 0, len(inorder) - 1)