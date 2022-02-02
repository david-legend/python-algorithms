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


print(find_max_in_bitonic_array([1, 3, 8, 12, 4, 2]))
print(find_max_in_bitonic_array([3, 8, 3, 1]))
print(find_max_in_bitonic_array([1, 3, 8, 12]))
print(find_max_in_bitonic_array([10, 9, 8]))

