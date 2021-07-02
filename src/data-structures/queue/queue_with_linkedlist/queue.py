# isEmpty(), enqueue(), dequeue(), peek(), delete()

class Node:
    def __init__(self, value = None):
        super().__init__()
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        super().__init__()
        self.head = None
        self.tail = None

    def __iter__(self):
        currentNode = self.head
        while currentNode:
            yield currentNode

            if (currentNode.next == None):
                break
            currentNode = currentNode.next

class Queue:
    def __init__(self):
        super().__init__()
        self.linkedlist = LinkedList()

    def __str__(self):
        values = [str(x) for x in self.linkedlist]
        return ' '.join(values)

    def enqueue(self, value):
        newNode = Node(value)
        if self.isEmpty():
            self.linkedlist.head = newNode
            self.linkedlist.tail = newNode
        else:
            self.linkedlist.tail.next = newNode
            self.linkedlist.tail = newNode

    def dequeue(self):
        if self.isEmpty():
            return None
        else:
            temp = self.linkedlist.head
            if(self.linkedlist.head == self.linkedlist.tail):
                self.linkedlist.head = None
                self.linkedlist.tail = None
            else:
                self.linkedlist.head = self.linkedlist.head.next
            return temp
            

    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.linkedlist.head


    def isEmpty(self):
        if self.linkedlist.head is None:
            return True
        else:
            return False

    def delete(self):
        self.linkedlist.head = None


queue = Queue()

print("is empty ? ", queue.isEmpty())

queue.enqueue(8)
queue.enqueue(18)
queue.enqueue(80)
queue.enqueue(19)

print("Current Queue: ", queue)
print("is empty ? ", queue.isEmpty())

print("Peek: ", queue.peek())
print("Dequeue: ", queue.dequeue())

print("Current Queue: ", queue)
print("Peek: ", queue.peek())

print("Dequeue: ", queue.dequeue())
print("Peek: ", queue.peek())

print("Delete: ", queue.delete())