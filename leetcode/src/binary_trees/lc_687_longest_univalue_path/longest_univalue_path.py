from collections import namedtuple

def longest_univalue_path(root):
    max_length = 0
    Data = namedtuple('Data', ['node', 'count'])
    def longest_univalue_path_helper(node):
        nonlocal max_length
        if not node: return Data(None, 0)

        left_sum, right_sum = 0, 0
        left = longest_univalue_path_helper(node.left)
        if left.node and left.node.val == node.val:
            left_sum = left.count + 1
        
        right = longest_univalue_path_helper(node.right)
        if right.node and right.node.val == node.val:
            right_sum = right.count + 1
        
        max_length = max(max_length, left_sum + right_sum)
        return Data(node, max(left_sum, right_sum))


    longest_univalue_path_helper(root)
    return max_length