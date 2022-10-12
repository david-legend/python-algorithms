from heapq import *
from collections import deque

class Solution:
    def smallestFromLeaf(self, root):
        min_heap = []
        def helper(node, path):
            if node is None: return
            
            path.appendleft(self.num_to_char(node.val))
            
            if not node.left and not node.right:
                heappush(min_heap, ("".join(path)))
            else:   
                helper(node.left, path)
                helper(node.right, path)
            
            path.popleft()
            
        if root:  
            path = deque()
            helper(root, path)
            return heappop(min_heap)
        
        return ""
        
    def num_to_char(self, num):
        return chr(ord('a') + num)
            
            