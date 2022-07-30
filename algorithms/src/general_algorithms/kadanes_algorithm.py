# return the sum of the subarray with the maximum sum
def kadanes_algorithm(array):
    max_at_current_index, max_so_far = array[0], array[0]
    
    for num in array[1:]:
        max_at_current_index = max(num, max_at_current_index + num)
        max_so_far = max(max_so_far, max_at_current_index)
    
    return max_so_far


# return the subarray with the maximum sum
def kadanes_algorithm_2(array):
    max_at_current_index, max_so_far = array[0], array[0]
    start_idx, end_idx = 0, 0
    
    for i in range(1, len(array)):
        curr_sum = max_at_current_index + array[i]
        if array[i] > curr_sum and array[i] > max_so_far:
            start_idx = i
        max_at_current_index = max(array[i], curr_sum)
        
        if max_so_far < max_at_current_index:
            end_idx = i
        max_so_far = max(max_so_far, max_at_current_index)
    
    return array[start_idx: end_idx+1]
    


print("Maximum Sum SubArray")
print(kadanes_algorithm([3, 5, -9, 1]))
print(kadanes_algorithm([3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]))
print(kadanes_algorithm([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]))
print(kadanes_algorithm([-10, -2, -9, -4, -8, -6, -7, -1, -3, -5]))
print(kadanes_algorithm([3, 4, -6, 7, 8]))

print("\n\nMax SubArray")
print(kadanes_algorithm_2([3, 5, -9, 1]))
print(kadanes_algorithm_2([3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]))
print(kadanes_algorithm_2([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]))
print(kadanes_algorithm_2([-10, -2, -9, -4, -8, -6, -7, -1, -3, -5]))
print(kadanes_algorithm_2([3, 4, -6, 7, 8]))
