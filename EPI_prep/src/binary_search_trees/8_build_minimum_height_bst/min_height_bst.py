class TreeNode:
    def __init__(self, val, left = None, right=None):
        self.val = val
        self.left, self.right = left, right


# Build Binary Search Tree Using Post Order Traversal
def build_min_height_bst(sorted_array):
    start, end = 0, len(sorted_array) - 1

    if len(sorted_array) == 0:
        return None

    def build_bst(start, end):
        if start > end:
            return
        
        mid = (start + end) // 2

        if 0 <= mid < len(sorted_array):
            left_subtree = build_bst(start, mid-1)
            right_subtree = build_bst(mid+1, end)

            return TreeNode(sorted_array[mid], left_subtree, right_subtree)

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