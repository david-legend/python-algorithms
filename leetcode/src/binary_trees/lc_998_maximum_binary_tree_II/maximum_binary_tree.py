# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Solution 1 - One Pass
def insertIntoMaxTree( root, val: int):
    def buildTree(node, val):
        if node is None: return TreeNode(val)
        
        if val > node.val:
            return TreeNode(val, node, None)
        
        node.right = buildTree(node.right, val)
        return node
    
    return buildTree(root, val)


# Solution 2 - Two Passes
def insertIntoMaxTree2(root, val: int):
        if not root: return
        data = []
        inorder(root, data)
        data.append(val)
        
        def buildTree(nums):
            if not nums: return 
            
            max_val = max(nums)
            max_val_idx = nums.index(max_val)
            
            left = buildTree(nums[ : max_val_idx])
            right = buildTree(nums[max_val_idx + 1 : ])
            
            return TreeNode(max_val, left, right)
        
        return buildTree(data)
    
def inorder(node, data):
    if node is None: return
    
    inorder(node.left, data)
    data.append(node.val)
    inorder(node.right, data)