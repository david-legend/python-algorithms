class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

def has_path_sum(tree, target):
    if tree is None:
        return False

    curr_target = target - tree.val
    if curr_target == 0 and tree.left is None and tree.right is None:
        return True
    
    return has_path_sum(tree.left, curr_target) or has_path_sum(tree.right, curr_target)


node_1 = Node(1)
node_2 = Node(2)
node_3 = Node(3)
node_4 = Node(4)
node_5 = Node(5)
node_6 = Node(6)
node_7 = Node(7)

node_1.left, node_1.right = node_2, node_3
node_2.left, node_2.right = node_4, node_5
node_3.left, node_3.right = node_6, node_7

print(has_path_sum(node_1, 8)) # True
print(has_path_sum(node_1, 10)) # True
print(has_path_sum(node_1, 19)) # False
print(has_path_sum(node_1, 7)) # True
print(has_path_sum(node_1, 27)) # False