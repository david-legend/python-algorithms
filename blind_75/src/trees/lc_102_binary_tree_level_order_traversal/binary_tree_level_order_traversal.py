from collections import deque

def level_order_traversal(root):
    if not root: return []

    queue, result = deque([root]), []
    while queue:
        level_size, data = len(queue), []
        for _ in range(level_size):
            curr = queue.popleft()
            data.append(curr.data)

            if curr.left: queue.append(curr.left)
            if curr.right: queue.append(curr.right)
        result.append(data)
        
    return result