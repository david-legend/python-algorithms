from collections import deque

def average_of_levels(root):
    queue = deque([root])
    result = []
    
    while queue:
        level_size = len(queue)
        total_sum = 0
        
        for _ in range(level_size):
            curr_node = queue.popleft()
            
            total_sum += curr_node.val
            if curr_node.left:
                queue.append(curr_node.left)
            
            if curr_node.right:
                queue.append(curr_node.right)
        
        result.append(total_sum / level_size)
    
    return result