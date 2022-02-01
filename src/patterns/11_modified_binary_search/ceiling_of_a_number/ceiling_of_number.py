
def search_ceiling_of_a_number(arr, key):
    n = len(arr) -1 
    start, end = 0, n 
    if key > arr[n]:
        return -1
    elif key <= arr[start]:
        return start
    
    while start <= end:
        middle = start + (end - start) // 2
        
        if key < arr[middle]:
            end = middle - 1
        elif key > arr[middle]:
            start = middle + 1
        else:
            return middle
        
    return start



print(search_ceiling_of_a_number([4, 6, 10], 6))
print(search_ceiling_of_a_number([1, 3, 8, 10, 15], 12))
print(search_ceiling_of_a_number([4, 6, 10], 17))
print(search_ceiling_of_a_number([4, 6, 10], -1))
print(search_ceiling_of_a_number([4, 6, 10], 5))
