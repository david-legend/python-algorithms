# Time complexity
# Since, we are reducing the search range by half at every step, 
# this means that the time complexity of our algorithm will be O(logN) 
# where ‘N’ is the total elements in the given array.

# Space complexity
# The algorithm runs in constant space O(1).

def binary_search(arr, key):
    start, end = 0, len(arr) -1 
    is_ascending = arr[end] > arr[start]
    
    while start <= end:
        middle = start + (end - start) // 2
        
        if arr[middle] == key:
            return middle
        
        if is_ascending:
            if key < arr[middle]:
                end = middle - 1
            else:
                start = middle + 1
        else:
            if key > arr[middle]:
                end = middle - 1
            else:
                start = middle + 1
    return -1

print(binary_search([4, 6, 10], 10))
print(binary_search([1, 2, 3, 4, 5, 6, 7], 5))
print(binary_search([10, 6, 4], 10))
print(binary_search([10, 6, 4], 4))
