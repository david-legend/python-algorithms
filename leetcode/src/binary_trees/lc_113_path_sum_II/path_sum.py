def path_sum(root, target_sum):
    def path_sum_helper(node, path, target):
        if node is None: return

        path.append(node.val)
        current_target = target - node.val
        if node.left is None and node.right is None and current_target == 0:
            result.append(list(path))
        else:
            path_sum_helper(node.left, path, current_target)
            path_sum_helper(node.right, path, current_target)
        
        path.pop()
        
    result = []
    path_sum_helper(root, [], target_sum)

    return result