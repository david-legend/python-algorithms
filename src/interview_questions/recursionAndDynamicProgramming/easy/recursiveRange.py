# RecusrsiveRange --> Write a recursive function that accepts a number and adds all the number from 0 to the number passed

def recursiveRange(n):
    assert n >= 0, "Number must be greater than or equal to 0"
    if n == 0:
        return 0
    else:
        return n + recursiveRange(n-1)


print(recursiveRange(6))  #ans --> 21
print(recursiveRange(10)) #ans --> 55