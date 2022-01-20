# Time complexity
# The time complexity of the algorithm is O(n).

# Space complexity
# Ignoring the space required for the output array, 
# the algorithm runs in constant space O(1).

def find_missing_numbers(nums):
    i, n = 0, len(nums)
    result = []
    while i < n:
        j = nums[i] - 1
        if nums[i] <= len(nums) and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    
    for i in range(n):
        if nums[i] != i+1:
            result.append(i+1)
            
    return result

print(find_missing_numbers([2, 3, 1, 8, 2, 3, 5, 1]))
print(find_missing_numbers([2, 4, 1, 2]))
print(find_missing_numbers([2, 3, 2, 1]))