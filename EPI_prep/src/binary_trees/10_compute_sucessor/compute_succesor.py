
# Key Notes
# For example: 
#         3
#      /       \
#     4         5
#    / \       / \
#   2   9     6   7

# Point 1
# During an inorder traversal, each node that has a non empty right subtree 
# has its successor in that subtree.
# Take the tree, nodes 4, 3, 5 will always have their successor in their right 
# subtree because they have a non empty right subtree
# This node is the "left-most" node in that subtree, and can be computed by following 
# left children exclusively, stopping when there is no left child to continue from.

# Point 2
# If a node is its parent left child, it is guanranteed that the parent will be the next node we visit
# thus it's successor
# So taking the tree above as an example again, nodes - 2, 6 will always have their parents as the next node(successor)

# Point 3
# If the node is its parent's right child, then it means  we have already visited the parent.
# We can determine the next visited node by iteratively following parents, 
# stopping when we move up from a left child
# So taking the tree above, nodes: 9 and 7 will have their up the tree as we iteratively follow the parents


class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = self.parent = None

def compute_successor(node):
    if node:
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            
            return node
        
        while node.parent and node.parent.right is node:
            node = node.parent

        return node.parent
    
    return None


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


print(compute_successor(node_1)) # 6
print(compute_successor(node_2)) # 5
print(compute_successor(node_3)) # 7
print(compute_successor(node_4)) # 2
print(compute_successor(node_5)) # 1
print(compute_successor(node_6)) # 3
print(compute_successor(node_7)) # None