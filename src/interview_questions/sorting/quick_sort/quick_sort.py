# Time Complexity O(N * Log N)
# Space Complexity O(LogN)
def quick_sort(array):
    quick_sort_helper(array, 0, len(array)-1)
    return array

def quick_sort_helper(array, start, end):
    if start >= end:
        return
    
    pivot, left, right = start, start + 1, end
    
    while right >= left:
        if array[left] > array[pivot] and array[right] < array[pivot]:
            swap(left, right, array)
        
        if array[left] <= array[pivot]:
            left += 1
        
        if array[right] >= array[pivot]:
            right -= 1
    
    swap(pivot, right, array)
    quick_sort_helper(array, start, right - 1)
    quick_sort_helper(array, right+1, end)

def swap(i, j ,array):
    array[i], array[j] = array[j], array[i]

print(quick_sort([8, 5, 2, 9, 5, 6, 3]))
print(quick_sort([1]))
print(quick_sort([3, 1, 2]))
print(quick_sort([1, 2, 3]))