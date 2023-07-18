# Time O(2^N)
def house_robber(nums):
    def compute(idx):
        if idx < 0: return 0
        if idx == 0: return nums[0]

        rob = nums[idx] + compute(idx - 2)
        dont_rob = 0 + compute(idx-1)

        return max(rob, dont_rob)
    
    return compute(len(nums) - 1)

print(house_robber([2,1,4,9]))
print(house_robber([1,4,3,4,5]))
print("\n")



# Time O(N)
# Space O(N) + O(N)
def house_robber_memo(nums):
    def compute(idx, dp):
        if idx < 0: return 0
        if idx == 0: return nums[0]
        if dp[idx] != -1: return dp[idx]

        rob = nums[idx] + compute(idx - 2, dp)
        dont_rob = 0 + compute(idx-1, dp)

        dp[idx] = max(rob, dont_rob)
        return dp[idx]
    
    n = len(nums)
    dp = [-1] * n
    return compute(n - 1, dp)

print(house_robber_memo([2,1,4,9]))
print(house_robber_memo([1,4,3,4,5]))