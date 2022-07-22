# leetcode 96
class Node:
    def __init__(self, val, left = None, right = None) -> None:
        self.val = val
        self.left, self.right = left, right

def generate_binary_trees(n):
    if n <= 0:
        return [None]

    result = []
    for num_left_tree_nodes in range(n):
        num_right_tree_nodes = n - 1 - num_left_tree_nodes
        left_subtrees = generate_binary_trees(num_left_tree_nodes)
        right_subtrees = generate_binary_trees(num_right_tree_nodes)

        for left in left_subtrees:
            for right in right_subtrees:
                result.append(Node(0, left, right) )
        

    return result

# d = len(generate_binary_trees(2))

# def find():
#     result = [(left, right) for left in range(3) for right in range(3)]

#     return result

# print(find())
# print(d)
print(generate_binary_trees(3))