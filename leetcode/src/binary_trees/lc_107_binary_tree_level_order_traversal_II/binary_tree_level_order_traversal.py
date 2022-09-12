from collections import deque

def level_order_bottom(root):
    if not root:
            return []
        
    result = deque()
    queue = deque([root])
    while queue:
        level_size, level_data = len(queue), []
        for _ in range(level_size):
            curr_node = queue.popleft()
            level_data.append(curr_node.val)
            
            if curr_node.left:
                queue.append(curr_node.left)
            
            if curr_node.right:
                queue.append(curr_node.right)
                
        result.appendleft(level_data)
    
    return result