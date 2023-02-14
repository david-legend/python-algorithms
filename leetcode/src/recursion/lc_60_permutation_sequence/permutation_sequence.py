def getPermutation(n,  k):
    factorial = 1
    nums = []
    for i in range(1, n):
        factorial *= i
        nums.append(i)
    
    nums.append(n)
    result, k = [], k-1

    while True:
        next_val = nums[k//factorial]
        result.append(str(next_val))
        nums.remove(next_val)
        if(len(nums) == 0): break
        k = k % factorial
        factorial = factorial // len(nums)
    
    return "".join(result)

print(getPermutation(n = 3, k = 3))
print(getPermutation(n = 4, k = 17))
print(getPermutation(n = 4, k = 9))
print(getPermutation(n = 3, k = 1))