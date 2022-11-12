# Time complexity
# Since, we are reducing the search range by half at every step, 
# this means that the time complexity of our algorithm will be O(logN) 
# where ‘N’ is the total elements in the given array.

# Space complexity
# The algorithm runs in constant space O(1).
def find_max_in_bitonic_array(arr):
    start, end = 0, len(arr) - 1
    
    while start < end:
        mid = start + (end - start) // 2
        
        if arr[mid] > arr[mid + 1]:
            end = mid
        else:
            start = mid + 1
            
    return arr[start]

print("Concise Optimal Approach")
print(find_max_in_bitonic_array([1, 3, 8, 12, 4, 2]))
print(find_max_in_bitonic_array([3, 8, 3, 1]))
print(find_max_in_bitonic_array([1, 3, 8, 12]))
print(find_max_in_bitonic_array([10, 9, 8]))


def find_max(nums):
    n = len(nums)
    start, end = 0, n - 1
    while start <= end:
        mid = start + (end - start) // 2
        lower, upper = float('-inf'), nums[n-1]
        if mid - 1 >= 0: lower = nums[mid - 1]
        if mid + 1 < n: upper = nums[mid + 1]

        if nums[mid] >= lower and nums[mid] >= upper:
            return nums[mid]
        elif lower > nums[mid]:
            end = mid - 1
        else:
            start = mid + 1


print("\n\nPersonal Intuitive Approach")
print(find_max([1, 3, 8, 12, 4, 2]))
print(find_max([3, 8, 3, 1]))
print(find_max([1, 3, 8, 12]))
print(find_max([10, 9, 8]))