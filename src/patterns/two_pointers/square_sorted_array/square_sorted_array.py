# Time complexity O(N)

# Space complexity O(N)
# this space will be used for the output array
def square_and_sort_array(arr):
    length = len(arr)
    squares = [0 for x in range(length)]
    highest_idx = length - 1
    left, right = 0, length-1
    
    while left < right:
        left_square = arr[left] * arr[left]
        right_square = arr[right] * arr[right]
        
        if left_square > right_square:
            squares[highest_idx] = left_square
            left += 1
        else:
            squares[highest_idx] = right_square
            right -= 1
        
        highest_idx -= 1
    
    return squares


print("Squares: " + str(square_and_sort_array([-2, -1, 0, 2, 3])))
print("Squares: " + str(square_and_sort_array([-3, -1, 0, 1, 2])))