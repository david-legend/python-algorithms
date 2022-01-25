from collections import deque
from locale import currency

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse(root):
    result = []
    if not root:
        return []
    
    queue = deque()
    queue.append(root)
    
    while queue:
        level_size = len(queue)
        current_level = []
        for _ in range(level_size):
            curr_node = queue.popleft()
            current_level.append(curr_node.val)
            
            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)
        
        result.append(current_level)
            
    return result


root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
print("Level order traversal: " + str(traverse(root)))

