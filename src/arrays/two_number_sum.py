from test_cases import *

# Two Number Sum
# 
# Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. If any two numbers in the input array sum up to the target sum, the function should return them in an array, in any order. If no two numbers sum up to the target sum, the function should return an empty array.
# 
# Note that the target sum has to be obtained by summing two different integers in the array, you can't add a single integer to itself in order to obtain the target sum.
# 
# You can assume that there will be at most one pair of numbers summing up to the target sum.
# 
# Sample Input
#
# array=[3, 5, -4, 8, 11, 1, -1, 6]
# targetSum= 10

# Sample Output
# [-1, 11]




# Solution 1
# O(n^2) time & O(1) space
# Brute Force approach
def twoNumberSum(array, targetSum):
    if(len(array) > 0):
        # we use len(array) - 1 because we want to avoid using the same value in the array
        # For eg if we have [1, 2, 3, 4], 
        # this is to prevent using 4 and 4 in the last iteration
        for i in range(len(array) - 1): 
            firstNum = array[i]
            # we use range(i+1, len(array)) because we want to avoid using the same value in the array
            # For eg if we have [1, 2, 3, 4], 
            # when the outer loop is at 1, we dont want the inner loop to start at 1
            for j in range(i+1, len(array)):
                secondNum = array[j]
                if firstNum + secondNum == targetSum:
                    return [firstNum, secondNum]
       
        #return empty array if a match is not found
        return []



# Solution 2
# O(n) time & O(n) space

def twoNumberSum2(array, targetSum):
    table = {} #create hash table to track numbers
    for i in range(len(array)):
        x = array[i]
        # x + y = targetSum
        # y = targetSum - x
        y = targetSum - x 

        # after getting the corresponding value
        # check table and see if y exists, if not add x
        # continue this path till you find a y in the table
        if table.get(y) is None:
            table[x] = True
        else:
            #return values if y exist in table
            return [x, y]

    #return empty array if a match is not found
    return []



# Solution 3
# O(nLogN) time & O(1) space
def twoNumberSum3(array, targetSum):
    if(len(array) > 0):
        array.sort()
        left = 0
        right = len(array) - 1
        while left < right:
            currentSum = array[left] + array[right]
            if currentSum == targetSum:
                return [array[left], array[right]]
            elif currentSum < targetSum:
                left += 1
            elif currentSum > targetSum:
                right -= 1

    return []



print(twoNumberSum(twoNumberSumTestCase1["array"], twoNumberSumTestCase1["targetSum"]))  #Expected Output --> [-1, 11]
print(twoNumberSum(twoNumberSumTestCase2["array"], twoNumberSumTestCase2["targetSum"]))  #Expected Output --> [6, 4]
print(twoNumberSum(twoNumberSumTestCase3["array"], twoNumberSumTestCase3["targetSum"]))  #Expected Output --> [1, 4]
print(twoNumberSum(twoNumberSumTestCase4["array"], twoNumberSumTestCase4["targetSum"]))  #Expected Output --> [-3, 6]
print(twoNumberSum2(twoNumberSumTestCase5["array"], twoNumberSumTestCase5["targetSum"]))  #Expected Output --> [9, 8]
print(twoNumberSum2(twoNumberSumTestCase6["array"], twoNumberSumTestCase6["targetSum"]))  #Expected Output --> [15, 3]
print(twoNumberSum2(twoNumberSumTestCase7["array"], twoNumberSumTestCase7["targetSum"]))  #Expected Output --> [0, -5]
print(twoNumberSum2(twoNumberSumTestCase8["array"], twoNumberSumTestCase8["targetSum"]))  #Expected Output --> [-47, 210]
print(twoNumberSum3(twoNumberSumTestCase9["array"], twoNumberSumTestCase9["targetSum"]))  #Expected Output --> []
print(twoNumberSum3(twoNumberSumTestCase10["array"], twoNumberSumTestCase10["targetSum"]))  #Expected Output --> []
print(twoNumberSum3(twoNumberSumTestCase11["array"], twoNumberSumTestCase11["targetSum"]))  #Expected Output --> []
print(twoNumberSum3(twoNumberSumTestCase12["array"], twoNumberSumTestCase12["targetSum"]))  #Expected Output --> []