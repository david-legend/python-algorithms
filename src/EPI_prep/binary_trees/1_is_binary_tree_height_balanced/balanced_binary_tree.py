from collections import namedtuple

class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


def is_balanced_binary_tree(tree):
    BalancedTree = namedtuple('BalancedTree', ['is_balanced', 'height'])
    
    def check_balance(node):
        if not node:
            return BalancedTree(True, 0)
        
        left_subtree = check_balance(node.left)
        if left_subtree.is_balanced == False:
            return BalancedTree(False, 0)

        right_subtree = check_balance(node.right)
        if right_subtree.is_balanced == False:
            return BalancedTree(False, 0)

        is_balanced = abs(left_subtree.height - right_subtree.height)
        height = max(left_subtree.height, right_subtree.height) + 1

        return BalancedTree(is_balanced, height)

    return check_balance(tree).is_balanced

node_1 = Node(4)
node_2 = Node(-4)
node_3 = Node(-2)
node_4 = Node(7)
node_5 = Node(1)
node_6 = Node(6)

node_1.left, node_1.right = node_2, node_3
node_2.right = node_4
node_3.left = node_5
node_4.right = node_6

print(is_balanced_binary_tree(node_1)) #True


node_A = Node('A')
node_B = Node('B')
node_C = Node('C')
node_D = Node('D')
node_E = Node('E')
node_F = Node('F')
node_G = Node('G')
node_H = Node('H')
node_I = Node('I')

node_A.left, node_A.right = node_B, node_C
node_B.left, node_B.right = node_D, node_E
node_C.left, node_C.right = node_F, node_G

# print(is_balanced_binary_tree(node_A)) #True

node_D.left = node_H
node_H.left = node_I


# print(is_balanced_binary_tree(node_A)) #False