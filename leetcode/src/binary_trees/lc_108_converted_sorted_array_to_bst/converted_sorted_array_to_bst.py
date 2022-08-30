class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left, self.right = left, right


def convert_to_bst(sorted_array):
    start, end, n = 0, len(sorted_array) - 1, len(sorted_array)
    if n == 0: 
        return 
    
    def convert_to_bst_helper(start, end):
        if start > end:
            return
        
        mid = (start + end) // 2
        if 0 <= mid <= n-1:
            left = convert_to_bst_helper(start, mid - 1)
            right = convert_to_bst_helper(mid + 1, end)

            return Node(sorted_array[mid], left, right)

    return convert_to_bst_helper(start, end)


def inorder(root):
    if root is None:
        return 
    
    inorder(root.left)
    print(root.val, end=" ")
    inorder(root.right)


root = convert_to_bst([-10,-3,0,5,9])
inorder(root)