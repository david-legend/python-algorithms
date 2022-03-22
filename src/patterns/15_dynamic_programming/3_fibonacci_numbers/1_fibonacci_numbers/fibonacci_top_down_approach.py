# time complexity O(2^n)
# The time complexity of the above algorithm is exponential O(2^n)
# as we are making two recursive calls in the same function. 

# space complexity O(n)
# The space complexity is O(n) which is used to store the recursion stack.

def calculate_fib(n):
    if n < 2:
        return n
    
    return calculate_fib(n-1) + calculate_fib(n-2)



# Calculate Fibonacci with memoization
def calc_fib(n):
    dp = [-1 for x in range(n + 1)]
    return calc_fib_memoize(n, dp)

def calc_fib_memoize(n, dp):
    if n < 2:
        return n
    
    if dp[n] != -1:
        return dp[n]
    
    dp[n] = calc_fib_memoize(n-1, dp) + calc_fib_memoize(n-2, dp)
    return dp[n]




print("Recursive Solution Without Memoization")
print("5th Fibonacci is ---> " + str(calculate_fib(5)))
print("6th Fibonacci is ---> " + str(calculate_fib(6)))
print("7th Fibonacci is ---> " + str(calculate_fib(7)))

print("\n\nRecursive Solution With Memoization")
print("5th Fibonacci is ---> " + str(calc_fib(5)))
print("6th Fibonacci is ---> " + str(calc_fib(6)))
print("7th Fibonacci is ---> " + str(calc_fib(7)))