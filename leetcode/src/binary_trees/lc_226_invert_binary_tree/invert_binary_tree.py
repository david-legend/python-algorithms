class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left, self.right = left, right
    

# Best Case - Time O(n) | Space O(h)
# Worst Case - Time O(n) | Space O(n)
def invert_binary_tree(root):
    def invert_binary_tree_helper(node):
        if node is None:
            return
        
        left_result = invert_binary_tree_helper(node.left)
        right_result = invert_binary_tree_helper(node.right)

        #swap nodes after left and right subtrees traversal
        node.left, node.right = right_result, left_result

        return node
    
    return invert_binary_tree_helper(root)