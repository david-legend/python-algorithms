# Time - O(n)
# Space - O(n) + O(n) -> recursion stack + memoization space used
def fib(n):
    memo = [-1] * (n+1)
    fib_top_down(n, memo)

    return memo[n]


def fib_top_down(n, memo):
    if memo[n] != -1:
        return memo[n]
    
    if n == 0 or n == 1:
        memo[n] = n
        return memo[n]
    
    memo[n] = fib_top_down(n-1, memo) + fib_top_down(n-2, memo)
    return memo[n]




print(fib(7))  #13
print(fib(6))  #8
print(fib(5))  #5
print(fib(4))  #3
print(fib(3))  #2