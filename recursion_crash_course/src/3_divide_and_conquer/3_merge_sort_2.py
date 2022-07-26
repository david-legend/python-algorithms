def merge_sort(nums):
    n = len(nums)
    if n <= 1:
        return nums
    
    mid = n // 2
    left_array = nums[ : mid]
    right_array = nums[mid : ]

    return merge(merge_sort(left_array), merge_sort(right_array))


def merge(left_array, right_array):
    sorted_array = [None] * (len(left_array) + len(right_array))
    i = j = k = 0

    while i < len(left_array) and j < len(right_array):
        if left_array[i] <= right_array[j]:
            sorted_array[k] = left_array[i]
            i += 1
        else:
            sorted_array[k] = right_array[j]
            j += 1
        k += 1
    
    while i < len(left_array):
        sorted_array[k] = left_array[i]
        i += 1
        k += 1
    
    while j < len(right_array):
        sorted_array[k] = right_array[j]
        j += 1
        k += 1
    
    return sorted_array


print(merge_sort([8, 5, 2, 9, 5, 6, 3]))