# Time Complexity O(N^2)
# Space Complexity O(1)

def insertion_sort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            swap(j, j-1, array)
            j -= 1

    return array


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
    
    

print(insertion_sort([8, 5, 2, 9, 5, 6, 3]))
print(insertion_sort([1]))
print(insertion_sort([3, 1, 2]))
print(insertion_sort([1, 2, 3]))