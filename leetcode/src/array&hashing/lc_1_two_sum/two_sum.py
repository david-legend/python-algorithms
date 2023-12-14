def two_sum(nums, target):
    num_idx = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in num_idx:
            return [num_idx[diff], i]

        num_idx[nums[i]] = i
    
    return []


print(two_sum([2,7,11,15], 9))
print(two_sum([3,2,4], 6))
print(two_sum([3,3], 6))