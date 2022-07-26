# Time Complexity O(N^2)
# Space Complexity O(1)

def bubble_sort(array):
    is_sorted = False
    
    while not is_sorted:
        is_sorted = True
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                swap(i, i+1, array)
                is_sorted = False
    
    return array  
        

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
    

print(bubble_sort([8, 5, 2, 9, 5, 6, 3]))
print(bubble_sort([1]))
print(bubble_sort([3, 1, 2]))
print(bubble_sort([1, 2, 3]))