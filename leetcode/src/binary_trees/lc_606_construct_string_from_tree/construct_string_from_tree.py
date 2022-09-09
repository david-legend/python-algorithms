class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def treeStr(root):
    def treeStrHelper(node):
        result = str(node.val)

        if node.left:
            result += "(" + treeStrHelper(node.left) + ")"
        
        if node.right:
            if not node.left:
                result += "()"
            
            result += "(" + treeStrHelper(node.right) + ")"
        
        return result

    return treeStrHelper(root)