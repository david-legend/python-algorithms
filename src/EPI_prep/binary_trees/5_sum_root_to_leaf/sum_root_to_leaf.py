class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

def sum_root_to_leaf(tree):
    def sum(node, curr_sum):
        if node is None:
            return 0
        
        running_sum = curr_sum * 10 + node.val
        if node.left is None and node.right is None:
            return running_sum
        
        return sum(node.left, running_sum) + sum(node.right, running_sum)

    return sum(tree, 0)


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

print(sum_root_to_leaf(node_1))