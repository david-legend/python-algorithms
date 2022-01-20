# Time complexity
# The time complexity of the algorithm is O(n).

# Space complexity
# The algorithm runs in constant space O(1) but modifies the input array.

def find_duplicate(nums):
    i, n = 0, len(nums)
    
    while i < n:
        if nums[i] != i+1:
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                return nums[i]
        else:
            i += 1
    
    return -1


print(find_duplicate([1, 4, 4, 3, 2]))
print(find_duplicate([2, 1, 3, 3, 5, 4]))
print(find_duplicate([2, 4, 1, 4, 4]))