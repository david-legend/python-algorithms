from collections import namedtuple

class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

def lca(tree, node_1, node_2):
    Status = namedtuple('Status', ['num_target_nodes', 'ancestor'])

    def lca_helper(node):
        if node is None:
            return Status(0, None)
        
        left_result = lca_helper(node.left)
        if left_result.num_target_nodes == 2:
            return left_result
        
        right_result = lca_helper(node.right)
        if right_result.num_target_nodes == 2:
            return right_result
        
        num_target_nodes = left_result.num_target_nodes + right_result.num_target_nodes \
            + int(node is node_1) + int(node is node_2)
        
        return Status(num_target_nodes, node if num_target_nodes == 2 else None)

    return lca_helper(tree).ancestor

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

print(lca(node_1, node_4, node_5)) #2
print(lca(node_1, node_4, node_7)) #1
print(lca(node_1, node_2, node_5)) #3