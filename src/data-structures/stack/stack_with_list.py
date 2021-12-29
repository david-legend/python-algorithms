#methods 1. pop, push, peek, isEmpty, delete

class Stack:
    def __init__(self):
        super().__init__()
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)
        
    def push(self, value):
        self.list.append(value)

    def pop(self):
        if not self.isEmpty():
            return self.list.pop()

    def peek(self):
        if not self.isEmpty():
            return self.list[-1]


    def isEmpty(self):
        return self.list == []

    def delete(self):
        self.list = None

stack = Stack()

# Check if stack is empty
print(stack.isEmpty())

# Adding values to stack
stack.push(2)
stack.push(5)
stack.push(8)

# Check if stack is empty again
print(stack.isEmpty())

# Peek at element from stack
print(stack.peek())

# Pop element from stack
print(stack.pop())

print(stack.peek())

stack.delete()