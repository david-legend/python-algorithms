def max_product(nums):
    n = len(nums)
    if(n == 0): return 0

    result = float('-inf')
    for i in range(n):
        curr_val = nums[i]
        result = max(result, curr_val)
        sub_product = 1
        for j in range(i+1, n):
            sub_product *= nums[j]
            result = max(result, sub_product * curr_val)
    
    return result


print(max_product([2,3,-2,4])) # 6
print(max_product([-2,0,-1])) # 0
print(max_product([-2,0,5])) # 5
print(max_product([1,2,-3,0,-4,-5])) # 20
print(max_product([1,2,3,4,5,0])) # 120
print(max_product([2, -1, 0, 3, 1, -1])) # 3