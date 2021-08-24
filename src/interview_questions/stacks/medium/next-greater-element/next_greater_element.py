# Time  O(n) | Space  O(n)
def nextGreaterElement(array):
    result = [-1] * len(array)
    stack = []

    for idx in range(2 * len(array)):
        circularIdx = idx % len(array)

        while len(stack) > 0 and array[stack[len(stack) -1]] < array[circularIdx]:
            top  = stack.pop()
            result[top] = array[circularIdx]

        stack.append(circularIdx)

    return result


test1 = [2, 5, -3, -4, 6, 7, 2]
test2 = [0, 1, 2, 3, 4]
test3 = [6, 4, 5, 7, 2, 1, 3]
test4 = [7, 6, 5, 4, 3, 2, 1]
test5 = [1, 1, 1, 1, 1, 1, 1, 1]
test6 = [-9, 0, -5, 1, 3, -2, 18, 2, 5, 18]


print("Test 1\n")
print(nextGreaterElement(test1), "\n")  #result [5, 6, 6, 6, 7, -1, 5]

print("Test 2\n")
print(nextGreaterElement(test2), "\n")  #result [1, 2, 3, 4, -1]

print("Test 3\n")
print(nextGreaterElement(test3), "\n")  #result [7, 5, 7, -1, 3, 3, 6]

print("Test 4\n")
print(nextGreaterElement(test4), "\n")  #result [-1, 7, 7, 7, 7, 7, 7]

print("Test 5\n")
print(nextGreaterElement(test5), "\n")  #result [-1, -1, -1, -1, -1, -1, -1, -1]

print("Test 6\n")
print(nextGreaterElement(test6), "\n")  #result [0, 1, 1, 3, 18, 18, -1, 5, 18, -1]