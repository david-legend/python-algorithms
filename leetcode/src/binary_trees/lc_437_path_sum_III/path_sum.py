def path_sum(root, target_sum):
    def path_sum_helper(node, path):
        nonlocal count
        if node is None: return

        path.append(node.val)
        total_sum = 0
        for i in range(len(path) - 1, -1, -1):
            total_sum += path[i]
            if total_sum == target_sum:
                count += 1
        
        path_sum_helper(node.left, path)
        path_sum_helper(node.right, path)

        path.pop()
        
    count = 0
    path_sum_helper(root, [])
    return count