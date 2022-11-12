def findUnsortedSubarray(nums):
    n = len(nums)
    start, end = 0, n - 1

    while start < n-1 and nums[start] <= nums[start+1]:
        start += 1
    if start == n - 1:
        return 0
    while end > 0 and nums[end] >= nums[end-1]:
        end -= 1
    
    temp_window = nums[start : end+1]
    max_val = max(temp_window)
    min_val = min(temp_window)

    while start > 0 and nums[start-1] > min_val:
        start -= 1
    while end < n-1 and nums[end+1] < max_val:
        end += 1
    
    return end - start + 1


print(findUnsortedSubarray([2,6,4,8,10,9,15]))  #5
print(findUnsortedSubarray([1,2,3,4]))  #0
print(findUnsortedSubarray([1, 3, 2, 0, -1, 7, 10]))    #5
print(findUnsortedSubarray([1,3,2,2,2]))    #4
print(findUnsortedSubarray([3, 2, 1]))  #3