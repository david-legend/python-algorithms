class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time O(n) | Space O(n)

def create_list_of_leaves(tree):
    result = []
    def traverse_tree(node):
        if node is None:
            return []
        
        if node.left is None and node.right is None:
            result.append(node)
        
        traverse_tree(node.left)
        traverse_tree(node.right)
    
    traverse_tree(tree)
    return result


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