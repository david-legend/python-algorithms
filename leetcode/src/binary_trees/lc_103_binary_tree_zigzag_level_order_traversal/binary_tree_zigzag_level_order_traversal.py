from collections import deque

def zigzag_level_order(root):
    result = []
    if not root:
        return result
    
    queue = deque([root])
    left_to_right = True
    
    while queue:
        level_size, data = len(queue), deque()
        for _ in range(level_size):
            curr_node = queue.popleft()
            
            if left_to_right:
                data.append(curr_node.val)
            else:
                data.appendleft(curr_node.val)
            
            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)
                
        result.append(data)
        left_to_right = not left_to_right
    
    return result