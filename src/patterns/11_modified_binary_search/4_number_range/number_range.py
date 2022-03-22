# Time complexity
# Since, we are reducing the search range by half at every step, 
# this means that the time complexity of our algorithm will be O(logN) 
# where ‘N’ is the total elements in the given array.

# Space complexity
# The algorithm runs in constant space O(1).
def find_range(arr, key):
    result = [-1, -1]
    n = len(arr) - 1
    start, end = 0, n

    while start <= end:
        mid = start + (end - start) // 2
        
        if key == arr[mid]:
            start, end = mid, mid
            while arr[start] == key:
                start += 1
                if start > n:
                    break
            
            while arr[end] == key:
                end -= 1
                if end < 0:
                    break
                return [end+1, start-1]
        
        if key < arr[mid]:
            end = mid - 1
        elif key > arr[mid]:
            start = mid + 1


    return result


#Solution 2
def find_range_2(arr, key):
    result = [- 1, -1]
    result[0] = binary_search(arr, key, False)
    if result[0] != -1:  # no need to search, if 'key' is not present in the input array
        result[1] = binary_search(arr, key, True)
    return result


# modified Binary Search
def binary_search(arr, key, findMaxIndex):
    keyIndex = -1
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if key < arr[mid]:
            end = mid - 1
        elif key > arr[mid]:
            start = mid + 1
        else:  # key == arr[mid]
            keyIndex = mid
            if findMaxIndex:
                start = mid + 1  # search ahead to find the last index of 'key'
            else:
                end = mid - 1  # search behind to find the first index of 'key'

    return keyIndex

print(find_range_2([4, 6, 6, 6, 9], 6))
print(find_range([1, 3, 8, 10, 15], 10))
print(find_range([1, 3, 8, 10, 15], 12))