# Brute Force Solution

# Time Complexity - O(3^n) 
# The time complexity of the above algorithm is exponential O(3^n) 
# as we are making three recursive call in the same function. 

# Space Complexity - O(n) 
# The space complexity is O(n) which is used to store the recursion stack.
def count_ways(n):
    if n < 0:
        return 0
    if n == 0:
        return 1 # base case, we don't need to subtract any thing, so there is only one way
    if n == 1:
        return 1 # we take subtract 1 to be left with zero, and that is the only way
    if n == 2:
        return 1 # we can subtract 1 twice to get zero and that is the only way
    if n == 3:
        return 2 # '3' can be expressed as {1, 1, 1}, {3}
    
    subtract_1 = count_ways(n-1)
    subtract_3 = count_ways(n-3)
    subtract_4 = count_ways(n-4)
    
    return subtract_1 + subtract_3 + subtract_4


def count_ways_dp(n):
    dp = [-1 for _ in range(n+1)]
    return count_ways_recursive(n, dp)

def count_ways_recursive(n, dp):
    if n < 0:
        return 0
    if n == 0:
        return 1 # base case, we don't need to subtract any thing, so there is only one way
    if n == 1:
        return 1 # we take subtract 1 to be left with zero, and that is the only way
    if n == 2:
        return 1 # we can subtract 1 twice to get zero and that is the only way
    if n == 3:
        return 2 # '3' can be expressed as {1, 1, 1}, {3}
    
    if dp[n] != -1:
        return dp[n]
    
    subtract_1 = count_ways_recursive(n-1, dp)
    subtract_3 = count_ways_recursive(n-3, dp)
    subtract_4 = count_ways_recursive(n-4, dp)
    dp[n] = subtract_1 + subtract_3 + subtract_4
    return dp[n]

print("Recursive Solution Without Memoization")
print(count_ways(4))
print(count_ways(5))
print(count_ways(6))

print("\n\nRecursive Solution With Memoization")
print(count_ways_dp(4))
print(count_ways_dp(5))
print(count_ways_dp(6))