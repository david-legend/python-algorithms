def two_sum(nums, target):
    num_index =  {}
    
    for i, num in enumerate(nums):
        diff = target - num
        
        if diff in num_index:
            return [num_index[diff], i]
        
        num_index[num] = i
    
    return 


print(two_sum([2,7,11,15], 9))
print(two_sum([3,2,4], 6))
print(two_sum([3,3], 6))