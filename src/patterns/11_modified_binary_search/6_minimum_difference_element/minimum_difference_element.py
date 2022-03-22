def search_min_diff_element(arr, key):
    n = len(arr)
    start, end = 0, n-1
    
    if key > arr[end]:
        return arr[end]
    if key < arr[start]:
        return arr[start]
    
    while start <= end:
        mid = start + (end - start) // 2
        
        if key > arr[mid]:
            start = mid + 1
        elif key < arr[mid]:
            end = mid - 1
        else:
            return arr[mid]
    
    if (arr[start] - key) < (key - arr[end]):
        return arr[start]
    return arr[end]
   


print(search_min_diff_element([4, 6, 10], 7))
print(search_min_diff_element([4, 6, 10], 4))
print(search_min_diff_element([1, 3, 8, 10, 15], 12))
print(search_min_diff_element([4, 6, 10], 17))
