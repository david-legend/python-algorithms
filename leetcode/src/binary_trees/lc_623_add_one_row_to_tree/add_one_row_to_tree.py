from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def addOneRow(root, val: int, depth):
    if not root: return TreeNode(val)
    if depth == 1:
        new_root = TreeNode(val, root, None)
        return new_root
    
    queue, level = deque([root]), 1
    row_added = False
    while queue and not row_added:
        level_size = len(queue)
        for _ in range(level_size):
            curr = queue.popleft()
            
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
            
            if level == depth - 1:
                curr.left = TreeNode(val, curr.left)
                curr.right = TreeNode(val, None, curr.right)
                row_added = True
                
        level += 1
        
    return root