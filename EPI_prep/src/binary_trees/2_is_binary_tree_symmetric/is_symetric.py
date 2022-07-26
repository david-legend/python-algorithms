
class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

def is_symetric(tree):
    if tree is None:
        return True

    def check_symmetric(subtree_0, subtree_1):
        if subtree_0 is None and subtree_1 is None:
            return True
        elif subtree_0 and subtree_1:
            return (subtree_0.val == subtree_1.val \
                    and check_symmetric(subtree_0.left, subtree_1.right) \
                    and check_symmetric(subtree_0.right, subtree_1.left))

        # if one subtree is empty and the other is not
        return False

    return check_symmetric(tree.left, tree.right)



node_A = Node(314)
node_B = Node(6)
node_C = Node(2)
node_D = Node(3)
node_E = Node(6)
node_F = Node(2)
node_G = Node(3)


node_A.left, node_A.right = node_B, node_E
node_B.right = node_C
node_C.right, node_E.left = node_D, node_F
node_F.left = node_G

print(is_symetric(node_A))

node_C.val = 561
print(is_symetric(node_A))


node_F.left = None
print(is_symetric(node_A))