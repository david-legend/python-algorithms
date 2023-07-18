# Time O(N)
# Space O(N) + O(N) -> recursion stack + memoization space used
def climb(n):

    def solve(val):
        if val > n: return 0
        if dp[val] != -1: return dp[val]
        if val == n: return 1

        dp[val] = solve(val + 1) + solve(val + 2)
        return dp[val]

    dp = [-1] * (n+1)
    return solve(0)


print(climb(1)) #1
print(climb(2)) #2
print(climb(3)) #3
print(climb(4)) #5
print(climb(5)) #8 
