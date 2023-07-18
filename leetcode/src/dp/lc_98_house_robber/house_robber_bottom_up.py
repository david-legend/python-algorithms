# Time O(n)
# Space O(n)
def house_robber(nums):
    n = len(nums)
    dp = [-1] * n
    dp[0] = nums[0]

    for i in range(1, n):
        rob = nums[i] + (dp[i-2] if i > 1 else 0)
        dont_rob = 0 + dp[i-1]
        dp[i] = max(rob, dont_rob)
    
    return dp[n-1]

print(house_robber([2,1,4,9]))
print(house_robber([1,4,3,4,5]))
print("\n")


# Time O(N)
# Space O(1)
def house_robber_space_optimization(nums):
    n = len(nums)
    prev, prev_2 = nums[0], 0
    curr = 0

    for i in range(1, n):
        rob = nums[i] + (prev_2 if i > 1 else 0)
        dont_rob = 0 + prev
        curr = max(rob, dont_rob)
        prev, prev_2 = curr, prev
    
    return prev

print(house_robber_space_optimization([2,1,4,9]))
print(house_robber_space_optimization([1,4,3,4,5]))
print(house_robber_space_optimization([1,2]))