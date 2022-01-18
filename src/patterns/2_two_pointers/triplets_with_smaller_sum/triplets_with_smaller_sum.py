# Time complexity for the algorithms is O(N^2)

# Sorting the array will take O(N * logN). 
# The searchPair() function will take O(N). 
# As we are calling searchPair() for every number in the input array, 
# this means that overall searchTriplets() will take O(N * logN + N^2), 
# which is asymptotically equivalent to O(N^2).

# Space Complexity O(N)

# Ignoring the space required for the output array, 
# the space complexity of the above algorithm 
# will be O(N) which is required for sorting
def triplet_with_smaller_sum(arr, target):
    arr.sort()
    count = 0
    arr_length = len(arr)
    
    for i in range(arr_length - 2):
        count += search_pair(arr, arr[i], i+1, target)
                
    return count

def search_pair(arr, first, left, target_sum):
    count = 0
    right = len(arr) - 1
    
    while left < right:
        curr_sum = first + arr[left] + arr[right]
        
        if curr_sum < target_sum:
            count += right - left
            left += 1
        else:
            right -= 1
            
    return count

print(triplet_with_smaller_sum([-1, 0, 2, 3], 3)) # Output: 2
print(triplet_with_smaller_sum([-1, 4, 2, 1, 3], 5)) # Output: 4