def count_rotations(arr):
    start, end = 0, len(arr) - 1
    while start < end:
        mid = start + (end - start) // 2
        
        if mid < end and arr[mid] > arr[mid + 1]:
            return mid + 1
        
        if mid > start and arr[mid] < arr[mid - 1]:
            return mid
        
        if arr[start] < arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
        
    return 0

print(count_rotations([10, 15, 1, 3, 8]))
print(count_rotations([4, 5, 7, 9, 10, -1, 2]))
print(count_rotations([1, 3, 8, 10]))