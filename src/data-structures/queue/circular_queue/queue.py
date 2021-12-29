class Queue:
    def __init__(self, maxSize):
        super().__init__()
        self.items = maxSize * [None]
        self.maxSize = maxSize
        self.end = -1
        self.start = -1

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)

    def enqueue(self, value):
        if not self.isFull():
            # First check if queue is full, if it is full
            # Point end to the first element
            if (self.end + 1) == self.maxSize:
                self.end = 0
            else:
                # Increase end by 1 and use it as index for setting new value
                self.end += 1
                # Check if it is the first element being enqueued 
                # If it is, set start to 0
                if self.start == -1:
                    self.start = 0
                # Use end as index for setting the new value
                self.items[self.end] = value

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            firstItem = self.items[self.start]
            start = self.start

            # If there is only one item in the queue 
            # Set start and end to -1 after dequeuing
            if start == self.end:
                self.start = -1
                self.end = -1
            # if item being dequeued is the last item 
            # then set start to point to 0
            elif self.start + 1 == self.maxSize:
                self.start = 0 
            # Increase start pointer to point to the next item after dequeuing
            else:
                self.start += 1

            # Set location item being dequeued to None
            self.items[start] = None

            # Return dequeued Item
            return firstItem

    def front(self):
        if not self.isEmpty():
            return self.items[self.start]

    def rear(self):
        if not self.isEmpty():
            return self.items[self.end]
        
    def isFull(self):
        if (self.end + 1) == self.start:
            return True
        elif self.start == 0 and (self.end + 1) == self.maxSize:
            return True
        else:
            return False

    def isEmpty(self):
        if self.end == -1:
            return True
        else:
            return False

    def delete(self):
        self.items = self.maxSize * [None]
        self.start = -1
        self.end = -1


queue = Queue(4)

print("Is full ? ", queue.isFull())
print("Is Empty ? ", queue.isEmpty())

#Adding value to the queue
queue.enqueue(4)
queue.enqueue(8)
queue.enqueue(10)
queue.enqueue(18)

print(queue)
print("\nIs full ? ", queue.isFull())
print("Is Empty ? ", queue.isEmpty())

print("Dequeue: ", queue.dequeue())
print("front: ", queue.front())
print("Dequeue: ", queue.dequeue())
print("front: ", queue.front())

print("After Dequeuing Twice: ", queue)

print("Delete Queue: ", queue.delete())
print("After Deleting Queue: ", queue)
