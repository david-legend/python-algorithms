from collections import defaultdict


# inorder traversal
# Time O(n) | Space O(n)
def find_mode_in_bst(root):
    def find_mode_in_bst_helper(node):
        nonlocal count, max_count, prev
        if node is None: return

        find_mode_in_bst_helper(node.left)
        if prev is not None:
            if prev == node.val:
                count += 1
            else:
                count = 1
        
        if count > max_count:
            max_count = count
            modes.clear()
            modes.append(node.val)
        elif count == max_count:
            modes.append(node.val)
        
        prev = node.val
        find_mode_in_bst_helper(node.right)

    
    count, max_count, prev = 1, 0, None
    modes = []
    find_mode_in_bst_helper(root)

    return modes


# Preorder traversal
# Time O(n) | Space O(n)
def find_mode_in_bst_preorder(root):
    def find_mode_in_bst_helper(node):
        nonlocal max_count
        if node is None: return

        values_to_count[node.val] += 1
        count_to_values[values_to_count[node.val]].append(node.val)
        max_count = max(max_count, values_to_count[node.val])

        find_mode_in_bst_helper(node.left)
        find_mode_in_bst_helper(node.right)

    values_to_count, count_to_values = defaultdict(int), defaultdict(list)
    max_count = 0
    find_mode_in_bst_helper(root)
    
    return count_to_values[max_count]