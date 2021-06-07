# TRIPLE STEP: A child is running up a staircase with n steps 
# and can hop either 1 step, 2 steps, or 3 steps at a time. 
# Implement a method to count how many possible ways the child can run up the stairs.

# NOTE:: Regardless of whether or not you use memoization, note that the number of ways 
# will quickly overflow the bounds of an integer. By the time you get to just n 37, 
# the result has already overflowed. Using a long will delay, but not completely solve, this issue.

# Recursion with no memoization
def countWays(n):
    if(n < 0):
        return 0
    elif(n == 0):
        return 1
    else:
        return countWays(n-1) + countWays(n-2) + countWays(n-3) 

print(countWays(3))   #4 
print(countWays(4))   #7 
print(countWays(5))   #13 
print(countWays(10))  #274


# Recursion with memoization
def tripleStep(n):
    arr = [-1] * (n+1)
    return tripleStepImpl(n, arr)


def tripleStepImpl(n, arr):
    if(n < 0):
        return 0
    elif(n == 0):
        return 1
    elif(arr[n] > -1):
        return arr[n]
    else:
        arr[n] = tripleStepImpl(n-1, arr) + tripleStepImpl(n-2, arr) + tripleStepImpl(n-3, arr) 
        return arr[n]



print("\n\nTriple Step with Memoization")
print(tripleStep(3))   #4 
print(tripleStep(4))   #7 
print(tripleStep(5))   #13 
print(tripleStep(10))  #274