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

def traverse(root):
    result = []
    if root is None:
        return result

    queue = deque()
    queue.append(root)
    leftToRight = True
    
    while queue:
        level_size = len(queue)
        current_level = deque()
        for _ in range(level_size):
            current_node = queue.popleft()
            
            if leftToRight:
                current_level.append(current_node.val)
            else:
                current_level.appendleft(current_node.val)
            
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
           
                    
        result.append(list(current_level))
        leftToRight = not leftToRight
        
    return result



root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
root.right.left.left = TreeNode(20)
root.right.left.right = TreeNode(17)
print("Zigzag traversal: " + str(traverse(root)))

