def subset_sum(nums):
    result = []
    subset_sum_helper(nums, result, 0, 0)
    result.sort()
    return result

def subset_sum_helper(nums, result, idx, curr_sum):
    if idx >= len(nums):
        result.append(curr_sum)
        return
    
    subset_sum_helper(nums, result, idx + 1, curr_sum + nums[idx])
    subset_sum_helper(nums, result, idx + 1, curr_sum)




print(subset_sum([3,1,2]))
print(subset_sum([4,2,2,6]))