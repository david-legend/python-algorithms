# Write a recursive function to multiply two positive integers without using the * operator (or / operator). 
# You can use addition, subtraction, and bit shifting, but you should minimize the number of those operations.


#Brute Force Solution
def recursiveMultiply(a, b):
    if(b <= 0):
        return b
    return a + recursiveMultiply(a, b-1)


print(recursiveMultiply(3,7))


#TODO:: Add Optimal Solution