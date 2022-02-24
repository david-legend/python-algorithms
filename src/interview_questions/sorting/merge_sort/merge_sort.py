def merge_sort(array):
    n = len(array)
    if n <= 1:
        return array
    
    middle_idx = n // 2
    left_half = array[:middle_idx]
    right_half = array[middle_idx:]
    
    return merge_sort_helper(merge_sort(left_half), merge_sort(right_half))


def merge_sort_helper(left_half, right_half):
    sorted_array = [None] * (len(left_half) + len(right_half))
    i = j = k = 0
    
    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            sorted_array[k] = left_half[i]
            i += 1
        else:
            sorted_array[k] = right_half[j]
            j += 1
        k += 1
    
    while i < len(left_half):
        sorted_array[k] = left_half[i]
        i += 1
        k += 1
    
    while j < len(right_half):
        sorted_array[k] = right_half[j]
        j += 1
        k += 1
    
    return sorted_array

print(merge_sort([8, 5, 2, 9, 5, 6, 3]))
print(merge_sort([1]))
print(merge_sort([3, 1, 2]))
print(merge_sort([1, 2, 3]))