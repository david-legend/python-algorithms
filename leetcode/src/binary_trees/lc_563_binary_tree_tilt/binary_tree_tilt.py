from collections import namedtuple
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def binary_tree_tilt_simple(root):
    def binary_tree_tilt_helper(node):
        if node is None:
            return 0
        
        left = binary_tree_tilt_helper(node.left)
        right = binary_tree_tilt_helper(node.right)

        result[0] += abs(left - right)

        return left + right + node.val

    result = [0]
    binary_tree_tilt_helper(root)

    return result[0]




def binary_tree_tilt(root):
    Result = namedtuple('Result', ['children_sum', 'node_val'])
    def binary_tree_tilt_helper(node):
        nonlocal tilt_sum
        if node is None:
            return Result(0, 0)
        
        if node.left is None and node.right is None:
            return Result(0, node.val)

        left_result = binary_tree_tilt_helper(node.left)
        left_sum = left_result.children_sum + left_result.node_val

        right_result = binary_tree_tilt_helper(node.right)
        right_sum = right_result.children_sum + right_result.node_val

        tilt_sum += abs(left_sum - right_sum)
        
        return Result(left_sum + right_sum, node.val)

    tilt_sum = 0
    binary_tree_tilt_helper(root)

    return tilt_sum