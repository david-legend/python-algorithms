def length_of_longest_substring(arr, k):
    max_length, window_start = 0, 0
    max_ones_count = 0
    
    for window_end in range(len(arr)):
        curr_num = arr[window_end]
        if curr_num == 1:
            max_ones_count += 1

        if window_end - window_start + 1 - max_ones_count > k:
            if arr[window_start] == 1:
                max_ones_count -= 1
            window_start += 1
            
        max_length = max(max_length, window_end - window_start + 1)
    
    return max_length


print(length_of_longest_substring([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
print(length_of_longest_substring(
    [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))