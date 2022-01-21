def find_corrupt_pair(nums):
    i, n = 0, len(nums)
    
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    
    for i in range(n):
        if nums[i] != i+1:
            return [nums[i], i + 1]

    return [-1, -1]


print(find_corrupt_pair([3, 1, 2, 5, 2]))
print(find_corrupt_pair([3, 1, 2, 3, 6, 4]))
        