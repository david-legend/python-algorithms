class Node:
    def __init__(self, value = None):
        super().__init__()
        self.value = value
        self.prev = None
        self.next = None

    def getNext(self):
        return self.next

    def getPrev(self):
        return self.prev

    def getData(self):
        return self.value

    def setNext(self, node):
        self.next = node
    
    def setPrev(self, node):
        self.prev = node


class CircularDoublyLinkedList:
    
    def __init__(self):
        super().__init__()
        self.head = None