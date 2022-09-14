from collections import deque

def largestValues(root):
    if not root:
        return []
    
    queue, result = deque([root]), []
    while queue:
        level_size, max_node_val = len(queue), float('-inf')
        for _ in range(level_size):
            curr_node = queue.popleft()
            max_node_val = max(max_node_val, curr_node.val)
            
            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)
        result.append(max_node_val)
    return result