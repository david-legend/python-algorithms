# Time Complexity O(n)
# Sapce Complexity O(n)
def count_ways(n):
    if n < 2:
        return 1
    if n == 2:
        return 2
    
    dp = [0 for _ in range(n+1)]
    dp[0], dp[1], dp[2] = 1, 1, 2
    
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    
    return dp[n]

# Time Complexity O(n)
# Sapce Complexity O(1)
def count_ways_optimal(n):
    if n < 2:
        return 1
    if n == 2:
        return 2
    n1, n2, n3, temp = 1, 1, 2, 0
    
    for _ in range(3, n+1):
        temp = n1 + n2 + n3
        n1, n2, n3 = n2, n3, temp
    
    return temp
    
print("Bottom Up Dynamic Programming")
print(count_ways(3))
print(count_ways(4))
print(count_ways(5))

print("\n\nBottom Up Dynamic Programming With Memory Optimization")
print(count_ways(3))
print(count_ways(4))
print(count_ways(5))