# Time complexity
# Since, we are reducing the search range by half at every step, 
# this means that the time complexity of our algorithm will be O(logN) 
# where ‘N’ is the total elements in the given array.

# Space complexity
# The algorithm runs in constant space O(1).
def search_bitonic_array(arr, key):
    max_value_index = find_max(arr)
    if arr[max_value_index] == key:
        return max_value_index
    else:
        key_index = binary_search(arr, key, 0, max_value_index - 1, True)
        if key_index == -1:
            key_index = binary_search(arr, key, max_value_index + 1, len(arr)-1, False)
        return key_index


def find_max(arr):
    start, end = 0, len(arr) - 1
    while start < end:
        mid = start + (end - start) // 2
        if arr[mid] > arr[mid + 1]:
            end = mid
        else:
            start = mid + 1
    
    return start

def binary_search(arr, key, start, end, is_ascending):
    while start <= end:
        mid = start + (end - start) // 2
        
        if key == arr[mid]:
            return mid
        
        if is_ascending:
            if key > arr[mid]:
                start = mid + 1
            else:
                end = mid - 1
        else:
            if key > arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
                
    return -1

print(search_bitonic_array([1, 3, 8, 4, 3], 4))
print(search_bitonic_array([3, 8, 3, 1], 8))
print(search_bitonic_array([1, 3, 8, 12], 12))
print(search_bitonic_array([10, 9, 8], 10))