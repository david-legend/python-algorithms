class Node:
    def __init__(self, val, size = 0):
        self.val, self.size = val, size
        self.left = self.right = None


def kth_node(tree, k):
    if tree:
        while tree:
            left_size = tree.left.size if tree.left else 0
            if left_size + 1 < k:
                tree = tree.right
                k -= left_size + 1
            elif left_size == k - 1:
                return tree.val
            else:
                tree = tree.left
    
    return None
    

node_1 = Node(1, 7)
node_2 = Node(2, 3)
node_3 = Node(3, 3)
node_4 = Node(4, 1)
node_5 = Node(5, 1)
node_6 = Node(6, 1)
node_7 = Node(7, 1)

node_1.left, node_1.right = node_2, node_3
node_2.left, node_2.right = node_4, node_5
node_3.left, node_3.right = node_6, node_7


print(kth_node(node_1, 1))
print(kth_node(node_1, 2))
print(kth_node(node_1, 3))
print(kth_node(node_1, 4))
print(kth_node(node_1, 5))
print(kth_node(node_1, 6))
print(kth_node(node_1, 7))
