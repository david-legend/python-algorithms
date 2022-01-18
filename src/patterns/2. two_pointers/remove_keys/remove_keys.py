#Time complexity for this algorithm is O(N)
#Space complexity is O(1)
def remove_keys(arr, key):
    next_element = 0
    
    for i in range(len(arr)):
        if arr[i] != key:
            arr[next_element] = arr[i]
            next_element += 1
    
    return next_element


print(remove_keys([3, 2, 3, 6, 3, 10, 9, 3], 3)) #Output: 4
print(remove_keys([2, 11, 2, 2, 1], 2)) #Output: 2

