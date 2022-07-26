class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

def preorder_traversal(node):
    if node is None:
        return

    print(node.val)
    preorder_traversal(node.left)
    preorder_traversal(node.right)




def inorder_traversal(node):
    if node is None:
        return

    inorder_traversal(node.left)
    print(node.val)
    inorder_traversal(node.right)


def postorder_traversal(node):
    if node is None:
        return

    postorder_traversal(node.left)
    postorder_traversal(node.right)
    print(node.val)

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


print("\nnPreorder Traversal\n")
preorder_traversal(node_A) # A, B, D, E, C, F, G

print("\Inorder Traversal\n")
inorder_traversal(node_A) # D, B, E, A, F, C, G

print("\nPostorder Traversal\n")
postorder_traversal(node_A) # D, E, B, F, G, C, A
