# Time complexity
# The time complexity of the algorithm is O(N) 
# since we are iterating the input array only once.

# Space complexity
# The algorithm runs in constant space O(1).

def dutch_flag_sort(arr):
    low, high = 0, len(arr) - 1
    i = 0
    
    while i <= high:
        if arr[i] == 0:
            arr[i], arr[low] = arr[low], arr[i]
            low += 1
            i += 1
        elif arr[i] == 1:
            i += 1
        else:
            arr[i], arr[high] = arr[high], arr[i]
            high -= 1
    
    return arr


print(dutch_flag_sort([1, 0, 2, 1, 0]))  #Output: [0, 0, 1, 1, 2]
print(dutch_flag_sort([2, 2, 0, 1, 2, 0])) #Output: [0, 0, 1, 2, 2, 2,]