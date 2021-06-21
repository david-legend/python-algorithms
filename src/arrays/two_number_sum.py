from test_cases import *

#Brute Force approach
def twoNumberSum(array, targetSum):
    if(len(array) > 0):
        for i in range(len(array)):
            for j in range(len(array)):
                value = targetSum - array[i]
                if (value in array) and (value != array[i]):
                    return [value, array[i]]
        return []


print(twoNumberSum(twoNumberSumTestCase1["array"], twoNumberSumTestCase1["targetSum"]))  #Expected Output --> [-1, 11]
print(twoNumberSum(twoNumberSumTestCase2["array"], twoNumberSumTestCase2["targetSum"]))  #Expected Output --> [6, 4]
print(twoNumberSum(twoNumberSumTestCase3["array"], twoNumberSumTestCase3["targetSum"]))  #Expected Output --> [1, 4]
print(twoNumberSum(twoNumberSumTestCase4["array"], twoNumberSumTestCase4["targetSum"]))  #Expected Output --> [-3, 6]
print(twoNumberSum(twoNumberSumTestCase5["array"], twoNumberSumTestCase5["targetSum"]))  #Expected Output --> [9, 8]
print(twoNumberSum(twoNumberSumTestCase6["array"], twoNumberSumTestCase6["targetSum"]))  #Expected Output --> [15, 3]
print(twoNumberSum(twoNumberSumTestCase7["array"], twoNumberSumTestCase7["targetSum"]))  #Expected Output --> [0, -5]
print(twoNumberSum(twoNumberSumTestCase8["array"], twoNumberSumTestCase8["targetSum"]))  #Expected Output --> [-47, 210]
print(twoNumberSum(twoNumberSumTestCase9["array"], twoNumberSumTestCase9["targetSum"]))  #Expected Output --> []
print(twoNumberSum(twoNumberSumTestCase10["array"], twoNumberSumTestCase10["targetSum"]))  #Expected Output --> []
print(twoNumberSum(twoNumberSumTestCase11["array"], twoNumberSumTestCase11["targetSum"]))  #Expected Output --> []
print(twoNumberSum(twoNumberSumTestCase12["array"], twoNumberSumTestCase12["targetSum"]))  #Expected Output --> []