def remove_duplicates(arr):
    remove_dups = 1
    i = 1
    
    while i < len(arr):
        if arr[remove_dups - 1] != arr[i]:
            arr[remove_dups] = arr[i]
            remove_dups += 1
        
        i += 1
    
    return arr


print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
print(remove_duplicates([2, 2, 2, 11]))