class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def reconstruct_bst(preorder_sequence):
    root_idx = [0]
    def reconstruct_bst_helper(lower_bound, upper_bound):
        if root_idx[0] == len(preorder_sequence):
            return None
        
        root_value = preorder_sequence[root_idx[0]]

        if not (lower_bound <= root_value <= upper_bound):
            return None
        root_idx[0] += 1

        left_tree = reconstruct_bst_helper(lower_bound, root_value)
        right_tree = reconstruct_bst_helper(root_value, upper_bound)

        return TreeNode(root_value, left_tree, right_tree)

    return reconstruct_bst_helper(float('-inf'), float('inf'))


def preorder_traversal(node):
    if node is None:
        return

    print(node.val)
    preorder_traversal(node.left)
    preorder_traversal(node.right)

node = reconstruct_bst([43, 23, 37, 29, 31, 41, 47, 53])
print(preorder_traversal(node)) 
