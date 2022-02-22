# Brute Force Solution

# Time Complexity - O(3^n) 
# The time complexity of the above algorithm is exponential O(3^n) 
# as we are making three recursive call in the same function. 

# Space Complexity - O(n) 
# The space complexity is O(n) which is used to store the recursion stack.
def count_ways(n):
    if n < 0:
        return 0
    
    if n == 0 or n == 1:
        return 1
    if n == 2:
        return 2
    
    return count_ways(n-1) + count_ways(n-2) + count_ways(n-3)


# Optimal DP Solution (Top Down Approach)

# Time Complexity - O(n)
# Since our memoization array dp[n+1] stores the results for all the subproblems, 
# we can conclude that we will not have more than n+1 subproblems 
# (where ‘n’ represents the total number of steps). 
# This means that our time complexity will be O(N). 

# Space COmplexity - O(n)
# The space complexity will also be O(n); 
# this space will be used to store the recursion-stack.
def count_ways_dp(n):
    dp = [-1 for _ in range(n+1)]
    return count_ways_recursive(n, dp)


def count_ways_recursive(n, dp):
    if n < 0:
        return 0
    
    if n == 0 or n == 1:
        return 1
    if n == 2:
        return 2
    
    if dp[n] != -1:
        return dp[n]
    
    dp[n] = count_ways_recursive(n-1, dp) + count_ways_recursive(n-2, dp) + count_ways_recursive(n-3, dp)
    return dp[n]

print("Recursive Solution Without Memoization")
print(count_ways(3))
print(count_ways(4))
print(count_ways(5))

print("\n\nRecursive Solution With Memoization")
print(count_ways_dp(3))
print(count_ways_dp(4))
print(count_ways_dp(5))