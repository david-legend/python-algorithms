def sortStack(stack):
    # base case to end recursive calls
    if len(stack) == 0:
        return stack
	
    # get top value on the stack
    top = stack.pop() 
    sortStack(stack)
    # sort and insert value
    insertInSortedOrder(stack, top)
        
    return stack


def insertInSortedOrder(stack, value):
    # if incoming value is the last element or value is smaller 
    # or equal to the value on top of stack, then insert it because it is sorted
    if len(stack) == 0 or stack[len(stack) -1] <= value:
        stack.append(value)
        return

    # if the above condition is false, get top value and call insertInSortedOrder recursively
    top = stack.pop()
    insertInSortedOrder(stack, value)

    # after that, append value 
    stack.append(top)


test1 = [-5, 2, -2, 4, 3, 1]
test2 = [0, -2, 3, 4, 1, -9, 8]
test3 = [2, 4, 22, 1, -9, 0, 6, 23, -2, 1]
test4 = [-1, 0, 2, 3, 4, 1, 1, 1]
test5 = [3, 4, 5, 1, 2]
test6 = []


print("Input--> ", test1)
print("Sorted Output-->", sortStack(test1), "\n\n")

print("Input--> ", test2)
print("Sorted Output-->", sortStack(test2), "\n\n")

print("Input--> ", test3)
print("Sorted Output-->", sortStack(test3), "\n\n")

print("Input--> ", test4)
print("Sorted Output-->", sortStack(test4), "\n\n")

print("Input--> ", test5)
print("Sorted Output-->", sortStack(test5), "\n\n")

print("Input--> ", test6)
print("Sorted Output-->", sortStack(test6), "\n\n")