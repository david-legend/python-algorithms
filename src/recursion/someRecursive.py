# SomeRecursive --> Write a recursive function which accepts an array and a callback. 
# The function returns true if a single value in the array returns true when passed to the callback, otherwise it returns false

def isOdd(num):
    if num%2==0:
        return False
    else:
        return True

def someRecursive(arr, cb):
    arrLength = len(arr)
    assert arrLength > 0, "Length of array should be greater than 0"

    if(arrLength == 1):
        return cb(arr[0])
    
    ans = cb(arr[0])

    if(ans):
        return True
    else:
        return someRecursive(arr[1:], cb)


# Test
print(someRecursive([1,2,3,4], isOdd))  #ans --> True
print(someRecursive([4,6,8,9], isOdd))  #ans --> True
print(someRecursive([4,6,8], isOdd))    #ans --> False