#methods 1. pop, push, peek, isEmpty, isFull, delete

class Stack:
    def __init__(self, size):
        super().__init__()
        self.size = size
        self.list = []
        
    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)

    def push(self, value):
        if self.isFull():
            print("Stack is full")

        self.list.append(value)

    def pop(self):
        if self.list != [] and len(self.list) > 0:
            return self.list.pop()

        return None
        
    def peek(self):
        lastIndex = len(self.list) - 1
        if self.isEmpty():
            return None
        else:
            return self.list[lastIndex]


    def isEmpty(self):
        if self.list == []:
            return True

        return False

    def isFull(self):
        if len(self.list) == self.size:
            return True

        return False

    def delete(self):
        self.list = None



stack = Stack(3)

# Check if stack is empty
print("is empty? ", stack.isEmpty())

# Check if stack is Full
print("is full? ", stack.isFull())

# Adding values to stack
stack.push(2)
stack.push(5)
stack.push(8)

# Check if stack is empty
print("is empty? ", stack.isEmpty())

# Check if stack is Full
print("is full? ", stack.isFull())

# Peek at element from stack
print(stack.peek())

# Pop element from stack
print(stack.pop())

print(stack.peek())

stack.delete()