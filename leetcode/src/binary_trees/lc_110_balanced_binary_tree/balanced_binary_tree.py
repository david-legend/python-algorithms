from collections import namedtuple


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left, self.right = left, right


def is_balanced(root):
    Balanced = namedtuple('Balanced', ['height', 'is_balanced'])

    def is_balanced_helper(node):
        if node is None:
            return Balanced(0, True)
        
        left_result = is_balanced_helper(node.left)
        if not left_result.is_balanced:
            return left_result
        
        right_result = is_balanced_helper(node.right)
        if not right_result.is_balanced:
            return right_result
        
        is_balanced = abs(left_result.height - right_result.height) <= 1
        height = max(left_result.height, right_result.height) + 1

        return Balanced(height, True if is_balanced else False)

    return is_balanced_helper(root).is_balanced