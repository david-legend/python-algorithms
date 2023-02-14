def combination_sum(candidates, target):
    candidates.sort()
    result = []
    combination_sum_helper(0, target, candidates, [], result)

    return result


def combination_sum_helper(idx, target, candidates, path, result):
    if target == 0:
        result.append(list(path))
        return
    
    for i in range(idx, len(candidates)):
        curr_val = candidates[i]
        if i > idx and candidates[i-1] == curr_val: continue
        if target - curr_val < 0: break

        path.append(curr_val)
        combination_sum_helper(i+1, target - curr_val, candidates, path, result)
        path.pop()

print(combination_sum(candidates = [2,5,2,1,2], target = 5)) # [[1, 2, 2], [5]]
print(combination_sum(candidates = [10,1,2,7,6,1,5], target = 8)) # [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
print(combination_sum(candidates = [1,1,2], target = 4)) # [[1, 1, 2]]

  