from collections import deque

def findBottomLeftValue(root):
    queue = deque([root])
    
    left_most_val = None
    while queue:
        level_size = len(queue)
        for i in range(level_size):
            curr_node = queue.popleft()
            if i == 0:
                left_most_val = curr_node.val
            
            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)
                
    return left_most_val