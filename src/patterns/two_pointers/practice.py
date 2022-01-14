def square_and_sort_array(arr):
    arr_length = len(arr)
    squares = [0 for x in range(len(arr))]
    left_pointer, right_pointer = 0, arr_length - 1
    largest_idx = arr_length - 1
    
    while left_pointer < right_pointer:
        left_square = arr[left_pointer] * arr[left_pointer]
        right_square = arr[right_pointer] * arr[right_pointer]

        if left_square > right_square:
            squares[largest_idx] = left_square
            left_pointer += 1
        else:
            squares[largest_idx] = right_square
            right_pointer -= 1
        
        largest_idx -= 1
        
    return squares


print("Squares: " + str(square_and_sort_array([-2, -1, 0, 2, 3])))
print("Squares: " + str(square_and_sort_array([-3, -1, 0, 1, 2])))