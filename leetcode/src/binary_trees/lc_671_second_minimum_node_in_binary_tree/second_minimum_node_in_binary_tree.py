# Time O(n) | Space O(h)
def find_second_min_val(root):
    def find_second_min_val_helper(node):
        nonlocal min_val, second_min_val
        if node is None: return

        if node.val <= min_val:
            min_val = node.val
        elif node.val <= second_min_val:
            second_min_val = node.val
            
        find_second_min_val_helper(node.left)
        find_second_min_val_helper(node.right)

    min_val = second_min_val = float('inf')
    find_second_min_val_helper(root)

    return second_min_val if second_min_val != float('inf') else -1