from collections import deque
import math

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

def find_level_averages(root):
    result = []
    if root is None:
        return result
    
    queue = deque()
    queue.append(root)
    
    while queue:
        level_size = len(queue)
        level_max = -(math.inf)
        for _ in range(level_size):
            curr_node = queue.popleft()
            
            level_max = max(level_max, curr_node.val)
            
            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)
        
        result.append(level_max)
        
    return result



root = TreeNode(1)
root.left = TreeNode(20)
root.right = TreeNode(13)
root.left.left = TreeNode(3)
root.left.right = TreeNode(8)
root.right.left = TreeNode(7)
root.right.right = TreeNode(11)

print("Level averages are: " + str(find_level_averages(root)))
