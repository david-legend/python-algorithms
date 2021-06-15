# Magic Index: A magic index in an array A[ 1.•.n-1] is defined to be an index such that A[ i] = i. 
# Given a sorted array of distinct integers, 
# write a method to find a magic index, if one exists, in array A.

# ***FOLLOW UP
# What if the values are not distinct?

dataSet1 = [-23, -17, -11, -9, -7, 5]
dataSet2 = [23, 56, 98]
dataSet3 = [0, 1, 2, 3, 4, 5]


def magicFast(arr, start, end):
    if(end < start):
        return -1
    
    mid = int((start + end) / 2)

    if(arr[mid] == mid):
        return mid
    elif(arr[mid] > mid):
       return magicFast(arr, start, mid-1)
    elif(arr[mid] < mid):
        return magicFast(arr, mid+1, end)


print(magicFast(dataSet1, 0, len(dataSet1) - 1)) # 5
print(magicFast(dataSet2, 0, len(dataSet2) - 1)) # -1
print(magicFast(dataSet3, 0, len(dataSet3) - 1)) # 2



# FOLLOW UP --> What if the values are not distinct?

print("\n\nRunning for if values are not distinct")
dataSet4 = [-10, -5, 2, 2, 2, 3, 4, 7, 9, 12, 13]

def magicFast2(arr, start, end):
    if(end < start):
        return -1
    
    midIndex = int((start + end) / 2)
    midValue = arr[midIndex]
    if(midValue == midIndex):
        return midIndex
    

    # Search Left
    leftIndex = min(midIndex-1, midValue)
    left = magicFast2(arr, start, leftIndex)
    if(left >= 0):
           return left


    # Search Left
    rightIndex = min(midIndex+1, midValue)
    right = magicFast2(arr, rightIndex, end)
    return right

print(magicFast2(dataSet4, 0, len(dataSet3) - 1))

