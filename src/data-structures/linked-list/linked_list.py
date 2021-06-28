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

class LinkedList:
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
    
    def deleteLinkedList(self):
        if self.head == None:
            print("Singly Linked List does not exist")
        else:
            self.head = None

linkedList = linkedList()

# Insertions
newVal = Node(23)
linkedList.push(Node(1))
linkedList.push(newVal)
linkedList.append(2)
linkedList.append(47)
linkedList.insertAfter(newVal, 99)

# Print List
linkedList.printSLList()

# Print Size of linkedList
print("SIZE IS: ", linkedList.size())

# Search & delete operations
print("SEARCHING: ",linkedList.search(99).value)
linkedList.delete(2)

print([node.value for node in linkedList])

linkedList.deleteLinkedList()

print([node.value for node in linkedList])