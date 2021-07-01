#methods 1. pop, push, peek, isEmpty, delete
class Node:
    def __init__(self, value = None):
        super().__init__()
        self.value = value
        self.next = None

    def getNext(self):
        return self.next


    def getValue(self):
        return self.value



class LinkedList:

    def __init__(self):
        super().__init__()
        self.head = None

    def __iter__(self):
        currentNode = self.head

        while currentNode:
            yield currentNode
            if currentNode.next == None:
                break
            currentNode = currentNode.getNext()


class Stack:
    def __init__(self):
        super().__init__()
        self.linkedList = LinkedList()

    def __str__(self):
        values = [str(x.value) for x in self.linkedList]
        return '\n'.join(values)

    def push(self, value):
        node = Node(value)
        node.next = self.linkedList.head
        self.linkedList.head = node

    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.linkedList.head.value

    def pop(self):
        if self.isEmpty():
            return None
        else:
            value = self.linkedList.head.value
            self.linkedList.head = self.linkedList.head.getNext()
            return value


    def isEmpty(self):
        if self.linkedList.head == None:
            return True
        else:
            return False

    def delete(self):
        self.linkedList = None


stack = Stack()

# Testing isEmpty method of stack
print("is empty? ", stack.isEmpty())

# Testing pushing to stack
stack.push(4)
stack.push(5)
stack.push(6)

# Testing isEmpty method of stack again
print("is empty? ", stack.isEmpty())

print([node.value for node in stack.linkedList])

# Testing peek method of stack
print("PEEK: ", stack.peek()) #6

# Testing pop method of stack
print("POP: ", stack.pop()) #6

# Testing peek method of stack again
print("PEEK: ", stack.peek()) #5

print([node.value for node in stack.linkedList])

# Testing delete method of stack
print("delete ", stack.delete())
