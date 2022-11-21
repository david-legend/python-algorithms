class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sum_of_left_leaves(root):
    def sum_left_leaves_helper(node):
        if node is None:
            return False
        
        if node.left is None and node.right is None:
            return True
        
        left_result = sum_left_leaves_helper(node.left)
        if left_result:
            result[0] += node.left.val
        
        sum_left_leaves_helper(node.right)

    result = [0]
    sum_left_leaves_helper(root)

    return result[0]



# Solution 2
def sumOfLeftLeaves(root):
    def sumOfLeftLeavesHelper(node):
        nonlocal left_sum
        if node is None:
            return False
        
        if node.left:
            if node.left.left is None and node.left.right is None:
                left_sum += node.left.val
            else:
                sumOfLeftLeavesHelper(node.left)
        
            
        sumOfLeftLeavesHelper(node.right)
        
    left_sum = 0
    sumOfLeftLeavesHelper(root)
        
    return left_sum