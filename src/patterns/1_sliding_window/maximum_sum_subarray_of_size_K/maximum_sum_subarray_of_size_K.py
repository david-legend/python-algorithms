#Time complexity will be O(N).
#Space complexity O(1) (algorithm runs in constant space).
def max_sum_subarray(arr, k):
    arr_len = len(arr)
    if arr_len < k:
        return 0
    
    result = 0.0
    sum, start = 0.0, 0
    
    for i in range(arr_len):
        sum += arr[i]
        
        if i >= (k - 1):
            result = sum if sum > result else result
            sum -= arr[start]
            start += 1
            
    return result


result1 = max_sum_subarray([2, 1, 5, 1, 3, 2], 3)
print("Maximum sum of subarrays of size K: " + str(result1) + "\n\n")


result2 = max_sum_subarray([2, 3, 4, 1, 5], 2)
print("Maximum sum of subarrays of size K: " + str(result2) + "\n\n")