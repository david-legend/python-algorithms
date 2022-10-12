class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Solution 1
# Use Inbuilt max function
def construct_max_binary_tree(nums):
        def construct_tree(nums):
            if not nums:
                return 
            max_val = max(nums)
            max_val_idx = nums.index(max_val)
            
            left = construct_tree(nums[:max_val_idx])
            right = construct_tree(nums[max_val_idx + 1:])
            
            return TreeNode(max_val, left, right)
            
        return construct_tree(nums)


# Solution 2
# Implement your own getMax 
def constructMaximumBinaryTree(nums):
    max_num, max_num_idx = getMax(nums, 0, len(nums))
    def buildTree( start_idx, end_idx):
        if start_idx >= end_idx:
            return None
        
        curr_max_num, idx = getMax(nums, start_idx, end_idx)
        left = buildTree(start_idx, idx)
        right = buildTree(idx + 1, end_idx)
        
        return TreeNode(curr_max_num, left, right)
    
    
    root = TreeNode(max_num)
    root.left = buildTree(0, max_num_idx)
    root.right = buildTree(max_num_idx + 1, len(nums))
    
    return root
        
    
def getMax(nums, start, end):
    max_num, idx = nums[start], start
    
    for i in range(start, end):
        if nums[i] > max_num:
            max_num, idx = nums[i], i
    
    return (max_num, idx)