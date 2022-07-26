from collections import deque
import queue

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

def find_successor(root, key):
    if root is None:
        return None
    
    queue = deque()
    queue.append(root)
    
    while queue:
        currentNode = queue.popleft()
        # insert the children of current node in the queue
        if currentNode.left:
            queue.append(currentNode.left)
        if currentNode.right:
            queue.append(currentNode.right)

        # break if we have found the key
        if currentNode.val == key:
            break

    return queue[0] if queue else None


root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
result = find_successor(root, 12)

if result:
    print(result.val)
    
result = find_successor(root, 9)

if result:
    print(result.val)

