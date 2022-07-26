# Time complexity O(n)
# The time complexity of the algorithm is O(n). 
# Although we are not incrementing the index i when swapping the numbers, 
# this will result in more than n iterations of the loop, 
# but in the worst-case scenario, the while loop will swap a total of n-1 numbers, 
# and once a number is at its correct index, 
# we will move on to the next number by incrementing i. 
# So overall, our algorithm will take O(n) + O(n-1) 
# which is asymptotically equivalent to O(n).

# Space complexity O(1)
# The algorithm runs in constant space O(1).
def cyclic_sort(nums):
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
            
    return nums

print(cyclic_sort([3, 1, 5, 4, 2]))
print(cyclic_sort([2, 6, 4, 3, 1, 5]))
print(cyclic_sort([1, 5, 6, 4, 3, 2]))