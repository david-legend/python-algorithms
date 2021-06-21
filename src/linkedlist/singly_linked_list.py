class Node:
    def __init__(self, value = None):
        super().__init__()
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        super().__init__()
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    #Insertion into a linkedList
    def insert(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == -1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location-1:
                    tempNode = tempNode.next
                    index+1
                nextNode = tempNode.next
                tempNode.next = nextNode
                newNode.next = nextNode



singlyLinkedList = SinglyLinkedList()
singlyLinkedList.insert(4, 0)
singlyLinkedList.insert(5, 1)
singlyLinkedList.insert(6, 2)

print([node.value for node in singlyLinkedList])