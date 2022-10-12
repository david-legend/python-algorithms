from collections import deque

def widthOfBinaryTree(root):
    if not root: return 0
    
    queue = deque([(root, 1)])
    max_width = 0
    while queue:
        level_width = queue[-1][1] - queue[0][1] + 1
        max_width = max(max_width, level_width)
        level_size = len(queue)
        for _ in range(level_size):
            curr_node, idx = queue.popleft()
            
            if curr_node.left:
                queue.append((curr_node.left, 2 * idx))
            
            if curr_node.right:
                queue.append((curr_node.right, 2 * idx + 1))
    
    return max_width