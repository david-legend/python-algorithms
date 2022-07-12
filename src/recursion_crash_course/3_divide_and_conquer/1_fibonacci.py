
# Non optimized solution for Fibonacci
def fib(n):
    if n == 1 or n == 0:
        return n
    
    return fib(n-1) + fib(n-2)


# Optimized Fibonacci with caching
def fib_optimized(n):
    cache = {0: 0, 1: 1}
    
    def fib(n):
        if n in cache:
            return cache[n]
        
        computed = fib(n-1) + fib(n-2)
        cache[n] = computed
        return cache[n]
    
    return fib(n)

print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))

print("\nOptimized Fib")
print(fib_optimized(1))
print(fib_optimized(2))
print(fib_optimized(3))
print(fib_optimized(4))
print(fib_optimized(5))