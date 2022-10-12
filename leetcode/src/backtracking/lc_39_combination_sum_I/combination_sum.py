def combination_sum(candidates, target):
    def combination_helper(idx, curr_target, possible_candidates):
        if idx >= len(candidates):
            if curr_target == 0:
                result.append(list(possible_candidates))
            return
        
        if curr_target - candidates[idx] >= 0:
            possible_candidates.append(candidates[idx])
            combination_helper(idx, curr_target - candidates[idx], possible_candidates)
            possible_candidates.pop()
        
        combination_helper(idx + 1, curr_target, possible_candidates)
        
    result = []
    combination_helper(0, target, [])
    return result


print(combination_sum([2,3,4,7], 7)) #[[2, 2, 3], [3, 4], [7]]
print(combination_sum([2,3,5,8], 8)) #[[2, 2, 2, 2], [2, 3, 3], [3, 5], [8]]