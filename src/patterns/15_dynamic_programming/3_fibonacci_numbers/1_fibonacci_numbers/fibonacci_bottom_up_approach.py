# Time Complexity O(n)
# Sapce Complexity O(n)
def calculate_fibonacci(n):
    dp = [0, 1]
    for i in range(2, n+1):
        dp.append(dp[i-1] + dp[i-2])
    
    return dp[n] 


# Time Complexity O(n)
# Sapce Complexity O(1)
def calculate_fib(n):
    n1, n2, temp = 0, 1, 0
    for _ in range(n):
        temp = n1 + n2
        n1 = n2
        n2 = temp
    
    return n1
    
print("Bottom Up Dynamic Programming")
print("5th Fibonacci is ---> " + str(calculate_fibonacci(5)))
print("6th Fibonacci is ---> " + str(calculate_fibonacci(6)))
print("7th Fibonacci is ---> " + str(calculate_fibonacci(7)))

print("\n\Bottom Up Dynamic Programming with Memory Optimization")
print("5th Fibonacci is ---> " + str(calculate_fib(5)))
print("6th Fibonacci is ---> " + str(calculate_fib(6)))
print("7th Fibonacci is ---> " + str(calculate_fib(7)))