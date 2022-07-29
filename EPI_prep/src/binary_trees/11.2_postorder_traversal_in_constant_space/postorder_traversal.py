class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = self.parent = None

# There are parts of this function
# 1. When we are traversing down the tree
# 2. When we are traversing back up the tree
# 3. When we decide whether to traverse down the right subtree

# For this to happen we need to variables: prev & next
# As their names suggest at everypoint in time prev will point to where the tree has previously been
# And next will point to the next node we want to visit, this could be a left child, right child or parent(when traversing back up)
# For example: 
#         1
#      /       \
#     2         3
#    / \       / \
#   4   5     6   7

# taking the tree above prev will initialy be None but as we inorderly traverse down the tree, next will always point to the previous node
# the variables below present the order of what will be contained in prev & next
# prev = [None,   1    2,   4,   2,   5,   2,    1,   3,   6,   3,   7,      3,       1 ]
# curr = [1,      2,   4,   2,   5,   2,   1,    3,   6,   3,   7,   3,      1      None ]
# next = [2,      4,   2    5,   2,   1,   3,    6,   3,   7,   3,   1,     None]

# result= [4, 5, 2, 6, 7, 3, 1]


def post_order_traversal(tree):
    result, prev = [], None

    while tree:
        if prev is tree.parent:
            if tree.left:
                next = tree.left
            else:
                next = tree.right or tree.parent
                result.append(tree.val)
                
        elif prev is tree.left:
            next =  tree.right or tree.parent
        else:
            result.append(tree.val)
            next = tree.parent
        
        prev, tree = tree, next
    
    return result


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

node_2.parent, node_3.parent = node_1, node_1
node_4.parent, node_5.parent = node_2, node_2
node_6.parent, node_7.parent = node_3, node_3

print(post_order_traversal(node_1)) #[4, 5, 2, 6, 7, 3, 1]