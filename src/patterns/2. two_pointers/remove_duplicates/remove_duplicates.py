#Time complexity for this algorithm is O(N)
#Space complexity is O(1)
def remove_duplicates(arr):
    next_non_dup = 1
    i = 1
    
    while i < len(arr):
        if arr[next_non_dup - 1] != arr[i]:
            arr[next_non_dup] = arr[i]
            next_non_dup += 1
        
        i += 1
    
    return next_non_dup



print(remove_duplicates([2, 3, 3, 3, 6, 9, 9])) #Output 4 : because first four elements after removing the duplicates will be [2, 3, 6, 9]
print(remove_duplicates([2, 2, 2, 11])) # Output 2 : because first two elements after removing the duplicates will be [2, 11]