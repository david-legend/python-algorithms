class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


def max_depth(root):
    if root is None:
        return 0
    
    left_result = max_depth(root.left)
    right_result = max_depth(root.right)

    return max(left_result, right_result) + 1


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


print(max_depth(node_A)) #3