# Time O(n) + O(n)
# Space O(n) + O(n)
def house_robber(nums):
    n = len(nums)
    if n == 1: return nums[0]
    with_first, without_first =  [], []
    for i in range(n):
        if i != 0: without_first.append(nums[i])
        if i != n-1: with_first.append(nums[i])
    
    dp_with_first = [-1] * len(with_first)
    with_first_result = solve(len(with_first) - 1, with_first, dp_with_first)

    dp_without_first = [-1] * len(without_first)
    without_first_result = solve(len(without_first) - 1, without_first, dp_without_first)

    return max(with_first_result, without_first_result)


def solve(idx, nums, dp):
    if idx < 0: return 0
    if idx == 0: return nums[idx]
    if dp[idx] != -1: return dp[idx]

    rob = nums[idx] + solve(idx-2, nums, dp)
    dont_rob = 0 + solve(idx - 1, nums, dp)
    dp[idx] = max(rob, dont_rob)

    return dp[idx]


print(house_robber([2,3,2])) # 3
print(house_robber([1,2,3,1])) # 4
print(house_robber([1,2,3])) # 3