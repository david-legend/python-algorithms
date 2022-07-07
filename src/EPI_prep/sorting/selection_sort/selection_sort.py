
def selection_sort(array):
    n = len(array)
    current_idx = 0
    
    for i in range(current_idx, n-1):
        smallest_idx = i
        for j in range(current_idx+1, n):
            if array[smallest_idx] > array[j]:
                smallest_idx = j
        
        swap(smallest_idx, current_idx, array)
        current_idx += 1
                
    return array

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
    

print(selection_sort([8, 5, 2, 9, 5, 6, 3]))
print(selection_sort([1]))
print(selection_sort([3, 1, 2]))
print(selection_sort([1, 2, 3]))