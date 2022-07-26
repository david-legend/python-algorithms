def merge_sort(array):
    n = len(array)
    if n <= 1:
        return array
    
    middle_idx = n // 2
    left_array = array[ :middle_idx]
    right_array = array[middle_idx: ]
    
    return merge_sort_helper(merge_sort(left_array), merge_sort(right_array))

def merge_sort_helper(left_array, right_array):
    sorted_array = [None] * (len(left_array) + len(right_array))
    i = j = k = 0
    
    while i < len(left_array) and j < len(right_array):
        if left_array[i] <= right_array[j]:
            sorted_array[k] = left_array[i]
            i += 1
        else:
            sorted_array[k] = right_array[j]
            j += 1
        k += 1
    
    while i < len(left_array):
        sorted_array[k] = left_array[i]
        i += 1
        k += 1
    
    while j < len(right_array):
        sorted_array[k] = right_array[j]
        j += 1
        k += 1
        
    return sorted_array
    

print(merge_sort([8, 5, 2, 9, 5, 6, 3]))
print(merge_sort([1]))
print(merge_sort([3, 1, 2]))
print(merge_sort([1, 2, 3]))