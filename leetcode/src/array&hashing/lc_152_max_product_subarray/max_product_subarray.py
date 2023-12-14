def max_product(nums):
    n, result, prefix, suffix = len(nums), float('-inf'), 1, 1

    for i in range(n):
        if prefix == 0: prefix = 1
        if suffix == 0: suffix = 1

        prefix *= nums[i]
        suffix *= nums[n-i-1]
        result = max(result, max(prefix, suffix))
    
    return result


print(max_product([2,3,-2,4])) # 6
print(max_product([-2,0,-1])) # 0
print(max_product([-2,0,5])) # 5
print(max_product([1,2,-3,0,-4,-5])) # 20
print(max_product([1,2,3,4,5,0])) # 120
print(max_product([2, -1, 0, 3, 1, -1])) # 3