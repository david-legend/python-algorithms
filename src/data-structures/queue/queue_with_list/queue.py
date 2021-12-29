# isEmpty(), enqueue(), dequeue(), peek(), delete()
class Queue:
    def __init__(self):
        super().__init__()
        self.items = []
        
    def __str__(self):
        super().__str__()
        values = [str(x) for x in self.items]
        return ' '.join(values)

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop(0)

    def peek(self):
        if not self.isEmpty():
            return self.items[0]

    def isEmpty(self):
        return self.items == []

    def delete(self):
        self.items = []


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