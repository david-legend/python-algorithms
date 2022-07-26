from collections import namedtuple


class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


def kth_node(tree, k):
    Result = namedtuple('Result', ['status', 'node'])
    i = 0

    def inorder(node):
        nonlocal i
        if node is None:
            return Result(False, None)

        left_result = inorder(node.left)
        if left_result.status:
            return left_result

        i += 1
        if i == k:
            return Result(True, node)
        
        right_result = inorder(node.right)
        if right_result.status:
            return right_result
        
        return Result(False, None)

    
    return inorder(tree).node

def kth_node_2(tree, k):
    result = []

    def inorder(node):
        if node is None:
            return
        inorder(node.left)
        result.append(node)
        inorder(node.right)

    inorder(tree)
    return result[k-1] if k <= len(result) else None


    

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


print("\nKth Node First Solution\n")
print(kth_node(node_1, 1)) #4
print(kth_node(node_1, 2)) #2
print(kth_node(node_1, 3)) #5
print(kth_node(node_1, 4)) #1
print(kth_node(node_1, 5)) #6
print(kth_node(node_1, 6)) #3
print(kth_node(node_1, 7)) #7

print("\nKth Node Non Optimal Solution\n")
print(kth_node_2(node_1, 1)) #4
print(kth_node_2(node_1, 2)) #2
print(kth_node_2(node_1, 3)) #5
print(kth_node_2(node_1, 4)) #1
print(kth_node_2(node_1, 5)) #6
print(kth_node_2(node_1, 6)) #3
print(kth_node_2(node_1, 7)) #7
