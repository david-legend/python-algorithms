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



# push, append, insertAfter, search,    (delete, size, deleteLinkedList)
class CircularDoublyLinkedList:
    
    def __init__(self):
        super().__init__()
        self.head = None

    def __iter__(self):
        node = self.head
        while node:
            yield node

            if node.next == self.head:
                break
            node = node.getNext()

    def push(self, value):
        newNode = Node(value)
        temp = self.head

        newNode.next = self.head

        if self.head is not None:
            prev = self.head
            while temp:
                if temp == self.head:
                    temp.prev = newNode
                else:
                    temp.prev = prev

                if temp.next == self.head:
                    break

                prev = temp
                temp = temp.getNext()

            temp.next = newNode 
        else:
            newNode.next = newNode
        
        self.head = newNode

    def insertAfter(self, valueTobeInsertedAfter, value):
        if self.head == None:
            print("LinkedList is empty")
            return False

        newNode = Node(value)
        node = self.search(valueTobeInsertedAfter)

        if(node is not None):
            nextNode = node.getNext()
            node.next = newNode
            newNode.next = nextNode
            newNode.prev = node
            if nextNode != self.head:
                nextNode.prev = newNode
            return True

        return False

    def append(self, value):
        newNode = Node(value)
        if self.head == None:
            self.head = Node(value)
            newNode.next = newNode
            return


        currentNode = self.head
        prev = self.head

        while currentNode:
            if currentNode != self.head:
                currentNode.prev = prev
                
            if currentNode.next == self.head:
                break
            
            prev = currentNode
            currentNode = currentNode.getNext()

        currentNode.next = newNode
        newNode.next = self.head
        newNode.prev = currentNode

    def search(self, value):
        if self.head is None:
            return None

        currentNode = self.head
        found = False

        while currentNode:
            if currentNode.value == value:
                found = True
                break

            if currentNode.next == self.head:
                break
            
            currentNode = currentNode.getNext()

        if found:
            return currentNode

        return None;


    def size(self):
        if self.head == None:
            return 0

        current = self.head
        count = 0
        while current:
            if current.next == self.head:
                count += 1
                break

            count += 1
            current = current.getNext()

        return count

    def delete(self, value):
        if self.head == None:
            print("LinkedList is empty")
            return False

        current = self.head
        prevNode = self.head
        found = False

        while current:
            if current.value == value:
                found = True
                break
            if current.next == self.head:
                break

            prevNode = current
            current = current.getNext()

        if found:
            if prevNode == self.head:
                self.head = None
                return True
            else:
                prevNode.next = current.getNext()
                current.getNext().prev = prevNode
                return True

        return False

                
    def deleteLinkedList(self):
        if(self.head != None):
            self.head = None



circularDoublyLL = CircularDoublyLinkedList()

# Pushing Value to the beginning of a CircularDoublyLinkedList

circularDoublyLL.push(7)
circularDoublyLL.push(5)
circularDoublyLL.push(3)
circularDoublyLL.push(2)
circularDoublyLL.push(1)

circularDoublyLL.append(9)
circularDoublyLL.append(11)
circularDoublyLL.push(0)
circularDoublyLL.append(13)

circularDoublyLL.insertAfter(13, 45)
circularDoublyLL.insertAfter(0, 1)
circularDoublyLL.insertAfter(7, 8)

print("After Pushing ",[node.value for node in circularDoublyLL])


print("Search for 13, found: ", circularDoublyLL.search(13).value)
print("Search for 3, found: ", circularDoublyLL.search(3).value)
print("Search for 2, found: ", circularDoublyLL.search(2).value)


print("Size of linkedList is: ", circularDoublyLL.size())
# checking if nodes are pointing to the right nodes
# for node in circularDoublyLL:
#     if node.prev is not None:
#         print("PREVS:", node.prev.value, " <-- ", node.value)

# for node in circularDoublyLL:
#         print(node.value, " --> ", node.next.value)


circularDoublyLL.delete(7)
print("After deleting Node with value 7 --> ",[node.value for node in circularDoublyLL])

circularDoublyLL.deleteLinkedList()
print("After deleting LinkedList ",[node.value for node in circularDoublyLL])
