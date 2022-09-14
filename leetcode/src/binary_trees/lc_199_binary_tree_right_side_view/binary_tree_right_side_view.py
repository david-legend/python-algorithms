from collections import deque

def rightSideView(root):
    if not root:
        return []
    
    queue, result = deque([root]), []
    while queue:
        level_size = len(queue)
        for i in range(level_size):
            curr_node = queue.popleft()
            
            if i == level_size - 1:
                result.append(curr_node.val)
            
            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)
    
    return result