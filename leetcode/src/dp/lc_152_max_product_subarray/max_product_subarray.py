def max_product(nums):
    result = max(nums)
    currMax, currMin = 1, 1

    for num in nums:
        if num == 0:
            currMax, currMin = 1, 1
            continue
        tmp = currMax * num
        currMax = max(currMax * num, currMin * num, num)
        currMin = min(tmp, currMin * num, num)
        result = max(result, currMax)
    
    return result


print(max_product([2,3,-2,4])) # 6
print(max_product([-2,0,-1])) # 0
print(max_product([-2,0,5])) # 5
print(max_product([1,2,-3,0,-4,-5])) # 20
print(max_product([1,2,3,4,5,0])) # 120
print(max_product([2, -1, 0, 3, 1, -1])) # 3