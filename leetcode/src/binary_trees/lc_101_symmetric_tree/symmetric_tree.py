class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


def is_symmetric(root):
    def is_symmtric_helper(subtree1, subtree2):
        if subtree1 is None and subtree2 is None:
            return True
        elif subtree1 and subtree2:
            return subtree1.val == subtree2.val and \
                is_symmtric_helper(subtree1.left, subtree2.right) and \
                is_symmtric_helper(subtree1.right, subtree2.left)
        
        return False

    if root:
        return is_symmtric_helper(root.left, root.right)
    
    return False






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

print(is_symmetric(node_A))

node_C.val = 561
print(is_symmetric(node_A))


node_F.left = None
print(is_symmetric(node_A))