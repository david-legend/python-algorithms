# Time Complexity - O(N^3)

# Explanation
# Sorting the array will take O(N * logN). 
# The searchPair(), in this case, will take O(N^2) 
# the main while loop will run in O(N) 
# but the nested for loop can also take O(N) - this will happen 
# when the target sum is bigger than every triplet in the array.
# So, overall searchTriplets() will take O(N * logN + N^3), 
# which is asymptotically equivalent to O(N^3).

# Space Complexity O(N)

# Ignoring the space required for the output array, 
# the space complexity of the above algorithm 
# will be O(N) which is required for sorting

def triplet_with_smaller_sum(arr, target):
    arr.sort()
    triplets = []
    
    for i in range(len(arr) - 2):
        search_pairs(arr, arr[i], i+1, target, triplets)
    
    return triplets   
        

def search_pairs(arr, first, left, target, triplets):
    right  = len(arr) -1
    
    while left < right:
        curr_sum = first + arr[left] + arr[right]
        
        if curr_sum < target:
            for i in range(right, left, -1):
                triplets.append([first, arr[left], arr[i]])
            left += 1
        else:
            right -= 1


print(triplet_with_smaller_sum([-1, 0, 2, 3], 3)) # Output: [[-1, 0, 3], [-1, 0, 2]]
print(triplet_with_smaller_sum([-1, 4, 2, 1, 3], 5)) # Output: [[-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]]