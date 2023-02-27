class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

def traversals(root):
    def traverse_helper(node):
        if not node: return

        preorder.append(node.val)

        traverse_helper(node.left)
        inorder.append(node.val)

        traverse_helper(node.right)
        postorder.append(node.val)

    preorder, inorder, postorder = [], [], []
    traverse_helper(root)
    return [preorder, inorder, postorder]


node_A = Node('A')
node_B = Node('B')
node_C = Node('C')
node_D = Node('D')
node_E = Node('E')
node_F = Node('F')
node_G = Node('G')

node_A.left, node_A.right = node_B, node_C
node_B.left, node_B.right = node_D, node_E
node_C.left, node_C.right = node_F, node_G

print(traversals(node_A)) # [['D', 'E', 'B', 'F', 'G', 'C', 'A'],  preorder
#                            ['D', 'B', 'E', 'A', 'F', 'C', 'G'],  inorder
#                            ['A', 'B', 'D', 'E', 'C', 'F', 'G']   postorder
# ]