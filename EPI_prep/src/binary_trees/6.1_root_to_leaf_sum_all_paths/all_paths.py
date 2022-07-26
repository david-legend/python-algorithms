class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

def has_path_sum(tree, target):
    def find_paths(node, target, paths):
        if node is None:
            return 
        
        curr_target = target - node.val
        paths.append(node.val)

        if curr_target == 0 and node.left is None and node.right is None:
            result.append(list(paths))
            paths.pop()
            return 
        
        find_paths(node.left, curr_target, paths)
        find_paths(node.right, curr_target, paths)
        paths.pop()

    result = []
    find_paths(tree, target, [])
    return result


node_1 = Node(1)
node_2 = Node(2)
node_3 = Node(3)
node_4 = Node(4)
node_5 = Node(0)
node_6 = Node(6)
node_7 = Node(7)
node_8 = Node(-1)

node_1.left, node_1.right = node_2, node_3
node_2.left, node_2.right = node_4, node_5
node_3.left, node_3.right = node_6, node_7
node_7.left = node_8

print(has_path_sum(node_1, 7)) # [[1, 2, 4]]
print(has_path_sum(node_1, 3)) # [[1, 2, 0]]
print(has_path_sum(node_1, 10)) # [[1, 3, 6], [1,3,7, -1]]
print(has_path_sum(node_1, 19)) # []
print(has_path_sum(node_1, 27)) # []