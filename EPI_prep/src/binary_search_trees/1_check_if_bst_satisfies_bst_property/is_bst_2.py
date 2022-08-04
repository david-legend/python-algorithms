from collections import namedtuple, deque

class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# The problem with the first solution (is_bst.py) is we have to traverse the entire left subtree
# before we traverse the right subtree. So if the node violating the BST is in the right subtree
# we have to finish traversing the left subtree befor we check the right subtree

# But if use the BFS approach, we check if every level to confirm whether each node is following the BST property
# If not we are able to break early whether the node is on the right subtree. Hence we are able to save some time 

 
# Best Case: Time O(n) | Space O(h)
# 
# Worst Case: Time O(n) | Space O(n)
def is_bst_valid(tree):
    if tree:
        QueueEntry = namedtuple('QueueEntry', ('node', 'lower', 'upper'))

        bfs_queue = deque([QueueEntry(tree, float('-inf'), float('inf'))])

        while bfs_queue:
            curr_node = bfs_queue.popleft()
            if not(curr_node.lower <= curr_node.node.val <= curr_node.upper):
                return False

            if curr_node.node.left:
                bfs_queue.append(QueueEntry(curr_node.node.left, curr_node.lower, curr_node.node.val))
            
            if curr_node.node.right:
                bfs_queue.append(QueueEntry(curr_node.node.right, curr_node.node.val, curr_node.upper))
    
    return True


    

bst = TreeNode(19)
bst_1 = TreeNode(7)
bst_2 = TreeNode(43)
bst_3 = TreeNode(3)
bst_4 = TreeNode(11)
bst_5 = TreeNode(23)
bst_6 = TreeNode(47)
bst_7 = TreeNode(2)
bst_8 = TreeNode(5)
bst_9 = TreeNode(17)
bst_10 = TreeNode(37)
bst_11 = TreeNode(53)
bst_12 = TreeNode(13)
bst_13 = TreeNode(29)
bst_14 = TreeNode(41)
bst_15 = TreeNode(31)

bst.left, bst.right = bst_1, bst_2
# Left Subtree
bst_1.left, bst_1.right = bst_3, bst_4
bst_3.left, bst_3.right = bst_7, bst_8
bst_9.left, bst_4.right = bst_12, bst_9

# Right Subtree
bst_2.left, bst_2.right = bst_5, bst_6
bst_5.right = bst_10
bst_10.left, bst_10.right = bst_13, bst_14
bst_13.right = bst_15
bst_6.right = bst_11

print(is_bst_valid(bst))


bst_1.right = TreeNode(3)
print(is_bst_valid(bst))
