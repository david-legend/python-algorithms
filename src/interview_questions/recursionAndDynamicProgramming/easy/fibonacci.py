def fibonacci(n):
    assert n >= 0 and int(n) == n, "Fibonnaci number must be positive integer"
    if n in [0, 1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(3)) #ans --> 2
print(fibonacci(5)) #ans --> 5

# Fibonnaci with memoization
def callFib(n):
    return fibWithMemo(n, [0] * (n+1))


def fibWithMemo(n, memo):
    if n <= 1:
        return n

    if(memo[n] == 0):
        memo[n] = fibWithMemo(n-1, memo) + fibWithMemo(n-2, memo)

    return memo[n]


print("\nCalling Fibonacci with Memoization")

print(callFib(3))
print(callFib(5))
print(callFib(7))
print(callFib(40))



# Other Fibonnaci implementations using Iteration
def fibWithIteration(n):
    a = 0
    b = 1

    for i in range(2, n):
        c = a + b
        a = b
        b = c

    return a + b

print("\nCalling Fibonacci with Iteration")
print(fibWithIteration(3))
print(fibWithIteration(5))
print(fibWithIteration(7))
print(fibWithIteration(40))


def fibWithIteration2(n):
    if n in [0, 1]:
        return n

    memo = [0] * (n+1)
    memo[1] = 1

    for i in range(2, n+1):
        memo[i] = memo[i-1] + memo[i-2]

    return memo[n]


print("\nCalling Fibonacci with Iteration 2")
print(fibWithIteration2(3))
print(fibWithIteration2(5))
print(fibWithIteration2(7))
print(fibWithIteration2(40))