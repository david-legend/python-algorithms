class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

def traversals(root):
    if not root: return []
    preorder, inorder, postorder = [], [], []
    stack = [(root, 1)]

    while stack:
        node, traversal_type = stack.pop()
        
        if traversal_type == 1:
            preorder.append(node.val)
            stack.append((node, traversal_type + 1))
            if node.left:
                stack.append((node.left, 1))
        elif traversal_type == 2:
            inorder.append(node.val)
            stack.append((node, traversal_type + 1))
            if node.right:
                stack.append((node.right, 1))
        else:
            postorder.append(node.val)

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

print(traversals(node_A)) # [['A', 'B', 'D', 'E', 'C', 'F', 'G'],  preorder
#                            ['D', 'B', 'E', 'A', 'F', 'C', 'G'],  inorder
#                            ['D', 'E', 'B', 'F', 'G', 'C', 'A']  postorder
# ]