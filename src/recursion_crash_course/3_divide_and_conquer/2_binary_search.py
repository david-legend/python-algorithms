def binary_search(nums, left, right, target):
    if left > right:
        return -1

    mid = (left + right) // 2

    if nums[mid] == target:
        return mid
    
    if target < nums[mid]:
        return binary_search(nums, left, mid - 1, target)
    
    return binary_search(nums, mid + 1, right, target)


nums = [-1, 0, 1, 2, 4, 5, 6, 10]
print(binary_search(nums, 0, len(nums) - 1, -1)) #0
print(binary_search(nums, 0, len(nums) - 1, 2)) #3
print(binary_search(nums, 0, len(nums) - 1, 10)) #7
print(binary_search(nums, 0, len(nums) - 1, 5)) #5