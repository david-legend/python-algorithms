class MinMaxStack:
    def __init__(self):
        self.minMaxStack = []
        self.stack = []
		
    def peek(self):
        if len(self.stack):
            return self.stack[len(self.stack) - 1]

    def pop(self):
        if len(self.stack):
            self.minMaxStack.pop()
            return self.stack.pop()

    def push(self, number):
        newMinMax = {"min": number, "max": number}
        if len(self.minMaxStack):
            lastMinMax = self.minMaxStack[len(self.minMaxStack) - 1]
            newMinMax["min"] = min(lastMinMax["min"], number)
            newMinMax["max"] = max(lastMinMax["max"], number)
			
        self.minMaxStack.append(newMinMax)
        self.stack.append(number)

    def getMin(self):
        return self.minMaxStack[len(self.minMaxStack) - 1]["min"]

    def getMax(self):
        return self.minMaxStack[len(self.minMaxStack) - 1]["max"]



stack = MinMaxStack()
print("pushing 5", stack.push(5))
print("Min: ", stack.getMin())
print("Max: ", stack.getMax())
print("Peek: ",stack.peek())

print("\n")

print("Pusing 7: ",stack.push (7))
print("Min: ",stack.getMin())
print("Max: ",stack.getMax())
print("Peek: ",stack.peek ())

print("\n")

print("Pushing 2: ", stack.push(2))
print("Min: ", stack.getMin())
print("Max: ", stack.getMax())
print("Peek: ", stack.peek ())

print("\n")

print("Pop: ",stack.pop())
print("Pop: ",stack.pop())
print("Min: ",stack.getMin())
print("Max: ",stack.getMax())
print("Peek: ",stack.peek())