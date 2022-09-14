from collections import deque

# Time O(n) | Space O(n/2 + 1)
def connect(root):
    if not root:
        return root
    
    queue = deque([root])
    while queue:
        level_size, prev = len(queue), None
        for _ in range(level_size):
            curr_node = queue.popleft()
            
            if prev:
                prev.next = curr_node
                prev = prev.next
            else:
                prev = curr_node
            
            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)
    
    return root