# Time complexity O(n + k)
# The time complexity of the algorithm is O(n + k), 
# as the last two for loops will run for O(n) and O(k) times respectively.

# Space complexity
# The algorithm needs O(k) space to store the extraNumbers
def find_first_k_missing_positive(nums, k):
    missing_numbers = []
    i, n = 0, len(nums)
    
    while i < n:
        j = nums[i] - 1
        if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    
    extra_numbers = []
    for i in range(n):
        if i+1 != nums[i]:
            if len(missing_numbers) < k:
                missing_numbers.append(i+1)
                extra_numbers.append(nums[i])
    
    i = 1
    while len(missing_numbers) < k:
        missing_num = i+n
        if missing_num not in extra_numbers:
            missing_numbers.append(missing_num)
        
        i += 1
        
    return missing_numbers

print(find_first_k_missing_positive([3, -1, 4, 5, 5], k=3)) #Output: [1, 2, 6]
print(find_first_k_missing_positive([2, 3, 4], k=3)) #Output: [1, 5, 6]
print(find_first_k_missing_positive([-2, -3, 4], k=2)) #Output: [1, 2]