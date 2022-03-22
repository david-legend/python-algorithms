from __future__ import print_function
from collections import deque



# Time complexity
# The time complexity of the above algorithm is O(N), 
# where ‘N’ is the total number of nodes in the tree. 
# This is due to the fact that we traverse each node once.

# Space complexity
# The space complexity of the above algorithm will be O(N) 
# as we need to return a list containing the level order traversal. 
# We will also need O(N) space for the queue. 
# Since we can have a maximum of N/2 nodes at any level 
# (this could happen only at the lowest level), 
# therefore we will need O(N) space to store them in the queue.
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right, self.next = None, None, None

  # tree traversal using 'next' pointer
    def print_tree(self):
        print("Traversal using 'next' pointer: ", end='')
        current = self
        while current:
            print(str(current.val) + " ", end='')
            current = current.next


def connect_all_siblings(root):
    if root is None:
        return
    
    queue = deque()
    queue.append(root)
    prev_node, curr_node = None, None
    
    while queue:
        curr_node = queue.popleft()
        
        if prev_node:
            prev_node.next = curr_node
        prev_node = curr_node 
        
        if curr_node.left:
            queue.append(curr_node.left)

        if curr_node.right:
            queue.append(curr_node.right)
            
            
root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
connect_all_siblings(root)
root.print_tree()


