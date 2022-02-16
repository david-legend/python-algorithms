# Time Complexity O(N^2)
# Space Complexity O(1)

def insertion(array):
    for i in range(len(array)):
        j = i 
        while j > 0 and array[j-1] > array[j]:
            swap(j, j-1, array)
            j -= 1
    
    return array

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
    

print(insertion([8, 5, 2, 9, 5, 6, 3]))
print(insertion([1]))
print(insertion([3, 1, 2]))
print(insertion([1, 2, 3]))