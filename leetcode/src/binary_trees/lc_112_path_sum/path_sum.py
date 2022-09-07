class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left, self.right = left, right


def path_sum(root, target):
    def path_sum_helper(node, target):
        if node is None:
            return False
        
        curr_target = target - node.val
        if node.left is None and node.right is None and curr_target == 0:
            return True

        left = path_sum_helper(node.left, curr_target)
        right = path_sum_helper(node.right, curr_target)

        return left or right

    return path_sum_helper(root, target)



# Terminate early if we find a path
def path_sum_2(root, target):
    def path_sum_helper(node, target):
        if node is None:
            return False
        curr_target = target - node.val
        if node.left is None and node.right is None and curr_target == 0:
            return True

        left_result = path_sum_helper(node.left, curr_target)
        if left_result:
            return left_result
        
        right_result = path_sum_helper(node.right, curr_target)
        if right_result:
            return right_result
        
        return left_result or right_result

    return path_sum_helper(root, target)