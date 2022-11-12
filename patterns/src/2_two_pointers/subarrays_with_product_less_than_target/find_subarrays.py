def find_subarrays(nums, target):
    start, product, result = 0, 1, []
        
    for end in range(len(nums)):
        curr_val = nums[end]
        product *= curr_val
        
        if curr_val < target:
            result.append([curr_val])

        while product >= target and start <= end:
            product = product / nums[start]
            start += 1
        
        if product < target:
            s, e = start, end
            while e - s + 1 > 1:
                result.append(nums[s:e+1])
                s += 1
    
    return result


print(find_subarrays([2, 5, 3, 10], target=30))
print(find_subarrays([8, 2, 6, 5], target=50 ))
print(find_subarrays([10,5,2,6], 100))


# return length
def numSubarrayProductLessThanK(nums, k):
    start, product, result = 0, 1, 0
    for end in range(len(nums)):
        curr_val = nums[end]
        product *= curr_val

        while product >= k and start <= end:
            product = product / nums[start]
            start += 1
        
        if product < k:
            result += end - start + 1
    
    return result

print(numSubarrayProductLessThanK([10,5,2,6], 100)) #8
print(numSubarrayProductLessThanK([10,5,2,6, 1], 100)) #12
print(numSubarrayProductLessThanK([1,2,3], 0)) #0
print(numSubarrayProductLessThanK([2,2], 5)) #3