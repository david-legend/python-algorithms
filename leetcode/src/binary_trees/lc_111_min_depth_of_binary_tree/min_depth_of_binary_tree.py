from collections import deque
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left, self.right = left, right


# Breadth First Search -> Level Order Traversal Solution
# Time O(n) | Space O(n/2 + 1)
def min_depth_bfs(root):
    if root is None:
        return 0
    else:
        queue = deque([root])
        depth = 1

        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                curr_node = queue.pop()

                if curr_node.left is None and curr_node.right is None:
                    return depth
                
                if curr_node.left:
                    queue.append(curr_node.left)
                
                if curr_node.right:
                    queue.append(curr_node.right)
            
            depth += 1
            

# Time O(n) | Space O(h)
def min_depth_of_tree(root):

    def min_depth_helper(node):

        if node and node.left is None and node.right is None:
            return 1
        
        left_result = float('inf')
        if node.left:
            left_result = min_depth_helper(node.left)

        right_result = float('inf')
        if node.right:
            right_result = min_depth_helper(node.right)
        
        return min(left_result, right_result) + 1

    if root:
        return min_depth_helper(root)
    
    return 0