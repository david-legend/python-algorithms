import math

# SOLUTION 1 (BRUTE FORCE)
#Time complexity O(N^2)
#Space complexity O(N)
def smallest_subarray_with_greater_sum(arr, s):
    k =  1
    def _find_smallest_subarray(arr, s, k):
        if k > len(arr):
            return 0
        
        sum, start = 0.0, 0
        for i in range(len(arr)):
            sum  += arr[i]
            
            if i >= k - 1:
                if sum >= s:
                    return k
                sum -= arr[start]
                start += 1
        
        return _find_smallest_subarray(arr, s, k+1)
        
    return _find_smallest_subarray(arr, s, k)


# SOLUTION 2
#The time complexity of the above algorithm will be O(N). 
#The outer for loop runs for all elements, and 
#the inner while loop processes each element only once; therefore, 
#the time complexity of the algorithm will be O(N+N), 
#which is asymptotically equivalent to O(N).

#Time complexity O(N)
#Space complexity O(1)
def smallest_subarray_with_given_sum(arr, s):
    min_len = math.inf
    sum, start = 0.0, 0
    for window_end in range(len(arr)):
        sum += arr[window_end]
        
        while sum >= s:
            min_len = min(min_len, window_end - start + 1)
            sum -= arr[start]
            start += 1
    
    if min_len == math.inf:
        return 0
    
    return min_len
        


result1 = smallest_subarray_with_given_sum([2, 1, 5, 2, 3, 2], 7) #answer --> 2
print("Smallest subarray with greater sum length: " + str(result1) + "\n\n")


result2 = smallest_subarray_with_given_sum([2, 1, 5, 2, 8], 7) #answer --> 1
print("Smallest subarray with greater sum length: " + str(result2) + "\n\n")


result3 = smallest_subarray_with_greater_sum([2, 1, 5, 2, 3, 2], 7) #answer --> 2
print("Smallest subarray with greater sum length: " + str(result3) + "\n\n")


result4 = smallest_subarray_with_greater_sum([2, 1, 5, 2, 8], 7) #answer --> 1
print("Smallest subarray with greater sum length: " + str(result4) + "\n\n")
        
    
                