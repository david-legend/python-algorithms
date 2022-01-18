# Time complexity for the algorithms are O(N^2)
# Sorting the array will take O(N * logN). 
# The searchPair() function will take O(N). 
# As we are calling searchPair() for every number in the input array, 
# this means that overall searchTriplets() will take O(N * logN + N^2), 
# which is asymptotically equivalent to O(N^2).

# Space complexity ia O(N)
# Ignoring the space required for the output array, 
# the space complexity of the above algorithm will be O(N) 
# which is required for sorting.

def search_triplets(arr):
    arr.sort()
    triplets = []
    
    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        search_pair(arr, -arr[i], i+1, triplets)
    
    return triplets

def search_pair(arr, target_sum, left, triplets):
    right = len(arr) - 1
    while left < right:
        sum = arr[left] + arr[right]
        if sum == target_sum:
            triplets.append([-target_sum, arr[left], arr[right]])
            left += 1
            right -= 1
            
            while left < right and arr[left] == arr[left-1]:
                left += 1
            while left < right and arr[right] == arr[right+1]:
                right -= 1
        elif sum < target_sum:
            left += 1
        else:
            right -= 1
            
            
print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
print(search_triplets([-5, 2, -1, -2, 3]))