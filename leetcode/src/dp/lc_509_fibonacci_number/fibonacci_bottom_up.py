# Time - O(n)
# Space - O(n)
def fib(n):
    dp = [-1] * (n+1)
    dp[0] = 0
    if n > 0: dp[1] = 1
        
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]


# Time - O(n)
# Space - O(1)
def fib_optimized(n):
    if (n == 0): return 0
    prev_2, prev= 0, 1

    for _ in range(2, n+1):
        curr = prev_2 + prev
        prev_2, prev = prev, curr
    
    return prev

print(fib(7))  #13
print(fib(6))  #8
print(fib(5))  #5
print(fib(4))  #3
print(fib(3))  #2