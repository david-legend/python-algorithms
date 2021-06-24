class Node:
    def __init__(self, value = None):
        super().__init__()
        self.value = value
        self.next = None

    def getData(self):
        return self.value

    def getNext(self):
        return self.next

    def setNext(self, node):
        self.next = node

class SinglyLinkedList:
    def __init__(self):
        super().__init__()
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.getNext()

    def printSLList(self):
        node = self.head
        while(node):
            print(node.value)
            node = node.getNext()

    #insert at beginning of node
    def push(self, node):
        newNode = node
        newNode.next = self.head
        self.head = newNode

    def insertAfter(self, prevNode, value):
        newNode = Node(value)
        if prevNode is None:
            print("The given previous node must be in LinkedList.")
            return
        newNode.next = prevNode.getNext()
        prevNode.next = newNode

    def append(self, value):
        newNode = Node(value)

        if(self.head is None):
            self.head = newNode
            return

        nextNode = self.head
        while nextNode.next:
            nextNode = nextNode.getNext()

        nextNode.next = newNode

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.getNext()
        return count


    def search(self, value):
        current = self.head
        found = False

        while current and found == False:
            if(current.value == value):
                found = True
            else:
                current = current.getNext()

        if(found == False):
            raise ValueError("Data not in list")

        return current

    def delete(self, value):
        current = self.head
        previous = None
        deleted = False
        
        while current and deleted == False:
            if(current.value == value):
                deleted = True
            else:
                previous = current
                current = current.getNext()
        
        if(deleted == False):
            raise ValueError("Data not in list")

        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())



singlyLinkedList = SinglyLinkedList()

# Insertions
newVal = Node(23)
singlyLinkedList.push(Node(1))
singlyLinkedList.push(newVal)
singlyLinkedList.append(2)
singlyLinkedList.append(47)
singlyLinkedList.insertAfter(newVal, 99)

# Print List
singlyLinkedList.printSLList()

# Print Size of linkedList
print("SIZE IS: ", singlyLinkedList.size())

# Search & delete operations
print("SEARCHING: ",singlyLinkedList.search(99).value)
singlyLinkedList.delete(2)

print([node.value for node in singlyLinkedList])