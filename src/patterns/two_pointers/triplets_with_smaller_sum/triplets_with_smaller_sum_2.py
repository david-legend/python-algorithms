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