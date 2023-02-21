class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


def postorder_traversal(root):
    if not root: return
    result, stack = [], []
    curr, prev = root, None

    while curr or stack:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            curr = stack[-1]
            if curr.right is None or curr.right is prev:
                result.append(curr.val)
                stack.pop()
                prev, curr = curr, None
            else:
                curr = curr.right
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


print("\nPostorder Traversal\n")
print(postorder_traversal(node_A)) # D, E, B, F, G, C, A