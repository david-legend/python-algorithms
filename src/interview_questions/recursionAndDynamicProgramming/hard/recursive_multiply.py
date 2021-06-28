# Write a recursive function to multiply two positive integers without using the * operator (or / operator). 
# You can use addition, subtraction, and bit shifting, but you should minimize the number of those operations.


#Brute Force Solution
# def recursiveMultiply(a, b):
#     if(b <= 0):
#         return b
#     return a + recursiveMultiply(a, b-1)


# print(recursiveMultiply(3,7))


#TODO:: Something wrong with this implementation --> will fix later
def minProduct(a, b):
    bigger = b if a < b else a
    smaller = a if a < b else b

    return minProductHelper(smaller, bigger)


def minProductHelper(smaller, bigger):
    if(smaller == 0):
        return 0
    elif(smaller == 1):
        return bigger

    # Compute half. If uneven, compute other half. If even, double it. 
    s = smaller >> 1
    side1 = minProduct(s, bigger)
    side2 = side1

    if(smaller % 2 == 1):
        minProductHelper(smaller-s, bigger)

    return side1 + side2

print(minProduct(7,7))
# print(2, 3)
# print(2, 3)