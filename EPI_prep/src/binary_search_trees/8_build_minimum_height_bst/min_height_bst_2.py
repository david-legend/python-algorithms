class TreeNode:
    def __init__(self, val, left = None, right=None):
        self.val = val
        self.left, self.right = left, right


# Build Binary Search Tree Using Pre Order Traversal
def build_min_height_bst(sorted_array):
    start, end = 0, len(sorted_array) - 1

    if len(sorted_array) == 0:
        return None

    def build_bst(start, end):
        if start > end:
            return
        
        mid = (start + end) // 2

        return TreeNode(sorted_array[mid], build_bst(start, mid-1), build_bst(mid+1, end))

    return build_bst(start, end)


def inorder(tree):
    if tree is None:
        return
    
    inorder(tree.left)
    print(tree.val)
    inorder(tree.right)


print("Example 1")
result_1 = build_min_height_bst([1,2,3,4,5,6,7])
inorder(result_1)

print("\nExample 2")
result_2 = build_min_height_bst([34, 56, 89, 99, 100])
inorder(result_2)

print("\nExample 3")
result_3 = build_min_height_bst([47])
inorder(result_3)