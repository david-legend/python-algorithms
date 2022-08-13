class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def reconstruct_bst(postorder_sequence):
    postorder_len = len(postorder_sequence)
    root_idx = [postorder_len - 1]

    def reconstruct_bst_helper(lower_bound, upper_bound):
        if root_idx[0] == -1:
            return None
        
        root_value = postorder_sequence[root_idx[0]]

        if not (lower_bound <= root_value <= upper_bound):
            return None
        
        root_idx[0] -= 1

        right_subtree = reconstruct_bst_helper(root_value, upper_bound)
        left_subtree = reconstruct_bst_helper(lower_bound, root_value)

        return TreeNode(root_value, left_subtree, right_subtree)
    
    return reconstruct_bst_helper(float('-inf'), float('inf'))


def postorder_traversal(node):
    if node is None:
        return

    postorder_traversal(node.left)
    postorder_traversal(node.right)
    print(node.val)

node = reconstruct_bst([14, 18, 16, 24, 27, 26, 30, 38, 19])
print(postorder_traversal(node)) # [14, 18, 16, 24, 27, 26, 30, 38, 19]
