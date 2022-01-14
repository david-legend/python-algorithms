def triplet_with_smaller_sum(arr, target):
    arr.sort()
    count = 0
    arr_length = len(arr)
    
    for i in range(arr_length - 2):
        left = i+1
        right = arr_length - 1
        
        while left < right:
            target_diff = target - (arr[i] + arr[left] + arr[right])
            
            if target_diff > 0:
                count += 1
                
            if target_diff > 0:
                right -= 1
            else:
                left += 1
                
    return count


print(triplet_with_smaller_sum([-1, 0, 2, 3], 3)) # Output: 2
print(triplet_with_smaller_sum([-1, 4, 2, 1, 3], 5)) # Output: 4