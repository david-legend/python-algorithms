def combination_sum(candidates, target):
    candidates.sort()
    result = []
    combination_sum_helper(candidates, target, 0, result, [])

    return result


def combination_sum_helper(arr, target, idx, result, possible_candiates):
    if target == 0:
        result.append(list(possible_candiates))
        return
    
    
    for i in range(idx, len(arr)):
        curr_val = arr[i]

        if i > idx and curr_val == arr[i - 1]: continue
        if target - curr_val < 0: break

        possible_candiates.append(curr_val)
        combination_sum_helper(arr, target - curr_val, i + 1, result, possible_candiates)
        possible_candiates.pop()

# print(combination_sum([1,1,1,2,2], 3))
print(combination_sum([1,2,3,1], 3))

  