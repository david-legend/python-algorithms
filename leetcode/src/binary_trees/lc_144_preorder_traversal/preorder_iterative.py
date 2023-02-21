class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


def preorder_traversal(root):
    if not root: return []
    result, stack = [], [root]

    while stack:
        node = stack.pop()
        result.append(node.val)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result


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
print(preorder_traversal(node_A)) # A, B, D, E, C, F, G
