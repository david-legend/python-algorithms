import math

# Time complexity is O(N^2)
# Sorting the array will take O(N* logN). 
# Overall, the function will take O(N * logN + N^2), 
# which is asymptotically equivalent to O(N^2).

# Space complexity will be O(N)
def triplet_sum_close_to_target(arr, target_sum):
    arr.sort()
    smallest_diff = math.inf
    arr_len = len(arr)
    
    for i in range(len(arr) - 2):
        left = i+1
        right = arr_len - 1
        
        while left < right:
            target_diff = target_sum - (arr[i] + arr[left] + arr[right])
            
            if target_diff == 0:
                return target_sum
            
            if abs(target_diff) < abs(smallest_diff) or (abs(target_diff) == abs(smallest_diff) and target_diff > smallest_diff):
                smallest_diff = target_diff
                
            if target_diff > 0:
                left += 1
            else:
                right -= 1
                
    
    return target_sum - smallest_diff
            

# print(triplet_sum_close_to_target([4, 2, 1, 2], 10))
print(triplet_sum_close_to_target([-2, 0, 1, 2], 2))
print(triplet_sum_close_to_target([-3, -1, 1, 2], 1))
print(triplet_sum_close_to_target([1, 0, 1, 1], 100))