from __future__ import print_function
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

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

def tree_left_view(root):
    result = []
    if root is None:
        return result
    
    queue = deque()
    queue.append(root)
    
    while queue:
        level_size = len(queue)
        
        for i in range(level_size):
            curr_node = queue.popleft()
            
            if i == 0:
                result.append(curr_node)
                
            if curr_node.left:
                queue.append(curr_node.left)

            if curr_node.right:
                queue.append(curr_node.right)
                
    return result


root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
root.left.left.left = TreeNode(3)

result = tree_left_view(root)
print("Tree right view: ")
for node in result:
    print(str(node.val) + " ", end='')
