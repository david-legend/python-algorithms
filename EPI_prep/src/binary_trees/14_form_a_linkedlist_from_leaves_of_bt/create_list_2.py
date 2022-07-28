class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time O(n) | Space O(n)

def create_list_of_leaves(tree):
    if tree is None:
        return []
    if tree.left is None and tree.right is None:
        return [tree]

    return create_list_of_leaves(tree.left) + create_list_of_leaves(tree.right)


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

print(create_list_of_leaves(node_1))