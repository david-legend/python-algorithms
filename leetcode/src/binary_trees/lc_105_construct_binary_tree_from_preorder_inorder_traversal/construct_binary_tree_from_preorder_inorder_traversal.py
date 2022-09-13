class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left


def buildTree(preorder, inorder):
    inorder_values_to_index = {data: i for i, data in enumerate(inorder)}
    def buildTreeHelper(preorder_start, preorder_end, inorder_start, inorder_end):
        if preorder_start >= preorder_end or inorder_start >= inorder_end:
            return 
        
        node_val = preorder[preorder_start]
        root_index = inorder_values_to_index[node_val]
        left_subtree_size = root_index - inorder_start
        
        preorder_start += 1
        left_preorder_end = preorder_start + left_subtree_size
        left = buildTreeHelper(preorder_start, left_preorder_end, inorder_start, root_index)
        right = buildTreeHelper(left_preorder_end, preorder_end, root_index + 1, inorder_end)
        
        return TreeNode(node_val, left, right)
    
    return buildTreeHelper(0, len(preorder), 0, len(inorder))


buildTree([3,9,20,15,7], [9,3,15,20,7])