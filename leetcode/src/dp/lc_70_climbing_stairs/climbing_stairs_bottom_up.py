# Time O(N)
# Space O(N)
def climb(n):
    if n <= 2: return n
    dp = [-1] * (n+1)
    dp[n-1], dp[n-2] = 1, 2

    for i in range(n-3, -1, -1):
        dp[i] = dp[i+1] + dp[i+2]

    return dp[0]


print(climb(1)) #1
print(climb(2)) #2
print(climb(3)) #3
print(climb(4)) #5
print(climb(5)) #8 
