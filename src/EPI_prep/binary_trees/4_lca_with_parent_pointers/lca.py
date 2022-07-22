class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = self.parent = None

def lca(node_1, node_2):
    if not node_1 or not node_2:
        return node_1 or node_2
    
    n1, n2 = node_1, node_2

    #get depth of both nodes
    n1_depth, n2_depth = get_depth(node_1), get_depth(node_2)

    # find depth difference to see if they are on the same level
    depth_diff = abs(n1_depth - n2_depth)

    # if nodes are not on the same level
    if depth_diff > 0:
        # make n1 always point to the node with the heighest depth
        if n2_depth > n1_depth:
            n1, n2 = node_2, node_1
        
        # move n1 node to the same level as n2
        while n1.parent and depth_diff > 0:
            depth_diff -= 1
            n1 = n1.parent
    
    # if they point to the same node when on the same level,
    # then one node was the ancestor of the other, hence return one of them
    if n1 is n2: return n1

    # find common ancestor by iterating upwards the tree
    while n1 is not n2:
        n1, n2 = n1.parent, n2.parent

    return n1

def get_depth(node):
    depth = 0
    if node:
        temp = node
        # iterate upwards to the root to find the depth of a node
        while temp.parent:
            depth += 1
            temp = temp.parent 
    return depth


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

print(lca(node_4, node_5))
print(lca(node_4, node_7))
print(lca(node_2, node_6))
print(lca(node_3, node_5))