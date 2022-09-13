from collections import deque

def level_order_traversal(root):
    if not root:
        return []
        
    result = []
    queue = deque([root])
    while queue:
        level_size, data = len(queue), []
        for _ in range(level_size):
            curr_node = queue.popleft()
            data.append(curr_node.val)
            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)
                
        result.append(data)
    
    return result