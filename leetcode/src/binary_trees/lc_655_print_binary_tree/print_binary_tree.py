import math

class Solution:
    def printTree(self, root):
        tree_height = self.getTreeHeight(root) - 1
        rows = tree_height + 1
        cols = int(math.pow(2, tree_height + 1) - 1)
        matrix = [["" for _ in range(cols)] for _ in range(rows)]
        
        def fillMatrix(node, r, c):
            nonlocal tree_height
            if node is None: return
            
            matrix[r][c] = str(node.val)
            
            fillMatrix(node.left, r+1,  c - int(math.pow(2, tree_height - r - 1)))
            fillMatrix(node.right, r+1,  c + int(math.pow(2, tree_height - r - 1)))
        
        r, c = 0, (len(matrix[0]) - 1) // 2
        fillMatrix(root, r, c)
        return matrix
        
    
    def getTreeHeight(self, node):
        if node is None: return 0
        
        left = self.getTreeHeight(node.left)
        right = self.getTreeHeight(node.right)
        
        return max(left, right) + 1