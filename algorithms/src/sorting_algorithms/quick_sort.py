# Time Complexity O(N * Log N)
# Space Complexity O(LogN)

def quick_sort(array):
    quick_sort_helper(array, 0, len(array) - 1)
    return array

def quick_sort_helper(array, start_idx, end_idx):
    if start_idx >= end_idx:
        return
    
    pivot_idx = start_idx
    left_idx = start_idx + 1
    right_idx = end_idx
    
    while right_idx >= left_idx:
        if array[left_idx] > array[pivot_idx] and array[right_idx] < array[pivot_idx]:
            swap(right_idx, left_idx, array)
        
        if array[left_idx] <= array[pivot_idx]:
            left_idx += 1
        
        if array[right_idx] >= array[pivot_idx]:
            right_idx -= 1
            
    swap(pivot_idx, right_idx, array)
    quick_sort_helper(array, start_idx, right_idx - 1)
    quick_sort_helper(array, right_idx + 1, end_idx)
        

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
    

print(quick_sort([8, 5, 2, 9, 5, 6, 3]))
print(quick_sort([1]))
print(quick_sort([3, 1, 2]))
print(quick_sort([1, 2, 3]))