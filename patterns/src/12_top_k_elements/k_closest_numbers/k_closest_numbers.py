from heapq import *


# The time complexity of the above algorithm is O(logN + K*logK). 
# We need O(logN) for Binary Search and O(K*logK) to insert the 
# numbers in the Min Heap, as well as to sort the output array.

# Space complexity
# The space complexity will be O(K), 
# as we need to put a maximum of 2K numbers in the heap.

def find_closest_elements(arr, K, X):
    index = binary_search(arr, X)
    left, right = index - K, index + K
    
    left = max(left, 0)
    right = min(right, len(arr) - 1)
    
    min_heap = []
    for i in range(left, right+1):
        heappush(min_heap, (abs(arr[i] - X), arr[i]))
     
    result = []   
    for i in range(K):
        result.append(heappop(min_heap)[1])
        
    result.sort()
    return result


def binary_search(arr, key):
    start, end = 0, len(arr) - 1
    
    while start <= end:
        mid = start + (end - start) // 2
        if key == arr[mid]:
            return mid
        
        if key > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
    
    if start > 0:
        return start - 1
    
    return start


print("'K' closest numbers to 'X' are: " +
        str(find_closest_elements([5, 6, 7, 8, 9], 3, 7)))
print("'K' closest numbers to 'X' are: " +
    str(find_closest_elements([2, 4, 5, 6, 9], 3, 6)))
print("'K' closest numbers to 'X' are: " +
    str(find_closest_elements([2, 4, 5, 6, 9], 3, 10)))