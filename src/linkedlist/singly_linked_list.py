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

    def printSLList(self):
        node = self.head
        while(node):
            print(node)
            node = node.next

    #insert at beginning of node
    def push(self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode

    def insertAfter(self, prevNode, value):
        newNode = Node(value)
        if prevNode is None:
            print("The given previous node must be in LinkedList.")
            return
        newNode.next = prevNode.next
        prevNode.next = newNode

    def append(self, value):
        newNode = Node(value)

        if(self.head is None):
            self.head = newNode
            return

        nextNode = self.head
        while nextNode.next:
            nextNode = nextNode.next

        nextNode.next = newNode




singlyLinkedList = SinglyLinkedList()
singlyLinkedList.push(4)
singlyLinkedList.push(5)
singlyLinkedList.append(75)
singlyLinkedList.push(6)
singlyLinkedList.push(9)

print([node.value for node in singlyLinkedList])