class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# For example: 
#         1
#      /       \
#     2         3
#    / \       / \
#   4   5     6   7

def reconstruct(preorder, inorder):
    node_to_inorder_idx = {data: i for i, data in enumerate(inorder)}

    # Builds the subtree with preorder[preorder_start:preorder_end] and
    # inorder[inorder_start:inorder_end].
    def binary_tree_from_preorder_inorder_helper(preorder_start, preorder_end,
                                                 inorder_start, inorder_end):
                                                 
        if preorder_end <= preorder_start or inorder_end <= inorder_start:
            return None

        root_inorder_idx = node_to_inorder_idx[preorder[preorder_start]]
        left_subtree_size = root_inorder_idx - inorder_start

        node_val = preorder[preorder_start]

         # Recursively builds the left subtree.
        left_subtree =  binary_tree_from_preorder_inorder_helper(
                preorder_start + 1, preorder_start + 1 + left_subtree_size,
                inorder_start, root_inorder_idx)

        # Recursively builds the right subtree.
        right_subtree = binary_tree_from_preorder_inorder_helper(
                preorder_start + 1 + left_subtree_size, preorder_end,
                root_inorder_idx + 1, inorder_end)

        return TreeNode(node_val, left_subtree, right_subtree)

    return binary_tree_from_preorder_inorder_helper(preorder_start=0,
                                                    preorder_end=len(preorder),
                                                    inorder_start=0,
                                                    inorder_end=len(inorder))


node_1 = TreeNode(1)
node_2 = TreeNode(2)
node_3 = TreeNode(3)
node_4 = TreeNode(4)
node_5 = TreeNode(5)
node_6 = TreeNode(6)
node_7 = TreeNode(7)

node_1.left, node_1.right = node_2, node_3
node_2.left, node_2.right = node_4, node_5
node_3.left, node_3.right = node_6, node_7

tree = reconstruct([1, 2, 4, 5, 3, 6, 7], [4, 2, 5, 1, 6, 3, 7])

def preorder_traversal(node):
    result = []
    def preorder(node):
        if node is None:
            return

        result.append(node.val)
        preorder(node.left)
        preorder(node.right)
    
    preorder(node)
    return result

def inorder_traversal(node):
    result = []
    def inorder(node):
        if node is None:
            return

        inorder(node.left)
        result.append(node.val)
        inorder(node.right)
    
    inorder(node)
    return result

print(preorder_traversal(tree)) # [1, 2, 4, 5, 3, 6, 7]
print(inorder_traversal(tree)) # [4, 2, 5, 1, 6, 3, 7]