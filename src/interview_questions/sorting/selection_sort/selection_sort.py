def selection_sort(array):
    current_idx = 0
    
    while current_idx < len(array) - 1:
        smallest_idx = current_idx
        for i in range(current_idx+1, len(array)):
            if array[i] < array[smallest_idx]:
                smallest_idx = i
        
        swap(current_idx, smallest_idx, array)
        current_idx += 1
    
    return array

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
    

print(selection_sort([8, 5, 2, 9, 5, 6, 3]))
print(selection_sort([1]))
print(selection_sort([3, 1, 2]))
print(selection_sort([1, 2, 3]))