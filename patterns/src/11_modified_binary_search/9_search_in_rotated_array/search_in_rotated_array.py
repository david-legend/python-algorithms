# Time complexity
# Since, we are reducing the search range by half at every step, 
# this means that the time complexity of our algorithm will be O(logN) 
# where ‘N’ is the total elements in the given array.

# Space complexity
# The algorithm runs in constant space O(1).
def search_rotated_array(arr, key):
    start, end = 0, len(arr) - 1
    
    while start <= end:
        mid = start + (end - start) // 2
        
        if arr[mid] == key:
            return mid
        
        if arr[start] <= arr[mid]:
            if key >= arr[start] and key < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if key > arr[mid] and key <= arr[end]:
                start = mid + 1
            else:
                end = mid - 1
                
    return -1

print(search_rotated_array([10, 15, 1, 3, 8], 15))
print(search_rotated_array([4, 5, 7, 9, 10, -1, 2], 10))