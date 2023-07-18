# Time O(N)
# Space O(N)

def frog_jump(nums):
    n = len(nums)
    dp = [-1] * (n)
    dp[0] = 0
    for i in range(1, n):
        if i+1 == n: continue
        jump_1 = dp[i] + abs(nums[i] - nums[i+1])
        jump_2 = float('inf')
        if i+2 < n:
            jump_2 = dp[i] + abs(nums[i] - nums[i+2])
        dp[i] = min(jump_1, jump_2)

    return dp[n-1]



print(frog_jump([10, 50, 10])) # 0
print(frog_jump([10, 20, 30, 10]))  # 20
print(frog_jump([7, 4, 4, 2, 6, 6, 3, 4]))  # 7
print(frog_jump([4, 8, 3, 10, 4, 4]))  # 2
print(frog_jump([5, 2, 8, 1, 3, 6])) # 9
print(frog_jump([1, 2, 1, 3, 2])) # 1
print(frog_jump([10, 5, 15])) # 5
print(frog_jump([30, 10, 60, 10, 60, 50]))  # 40