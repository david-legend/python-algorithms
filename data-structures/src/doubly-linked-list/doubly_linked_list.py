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


class DoublyLinkedList:

    def __init__(self):
        super().__init__()
        self.head = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == None:
                break
            node = node.getNext()

    def pushNode(self, newNode):
        newNode.next = self.head
        newNode.prev = None

        if self.head is not None:
            self.head.prev = newNode
        
        self.head = newNode

    def pushValue(self, value):
        # 1 & 2: Allocate the Node & Put in the data
        newNode = Node(value)

        # 3. Make next of new node as head and previous as NULL
        newNode.next = self.head
        newNode.prev = None

        # 4. change prev of head node to new node 
        if self.head is not None:
            self.head.prev = newNode
        
        # 5. move the head to point to the new node
        self.head = newNode

    def size(self):
        if self.head == None:
            return 0

        currentNode = self.head
        count = 0
        while currentNode:
            count += 1
            if currentNode.next == None:
                break

            currentNode = currentNode.getNext()

        return count

    def append(self, value):
        newNode = Node(value)
       
        if self.head == None:
            self.head = newNode
        else:
            current = self.head
            while current:
                if(current.next == None):
                    break;
                else:
                    current = current.getNext()

            current.next = newNode
            newNode.prev = current

    def insertAfter(self, prevNode, value):
        newNode = Node(value)
        newNode.next = prevNode.getNext()
        newNode.prev = prevNode
        prevNode.next = newNode

    def search(self, value):
        if(self.head == None):
            print("Doubly Linked List is empty")
            return
        current = self.head
        found = False
        while current:
            if current.value == value:
                found = True
                break;

            if current.next == None:
                break;
            
            current = current.next
        if found:
            return current
        else:
            print("Couldn't Find Value in Doubly Linked List")
            return

    def delete(self, value):
        if self.head == None:
            print("Can't delete value from a Linked List that is already empty")
            return False
        
        current = self.head
        prevNode = self.head
        found = False

        while current:
            if current.value == value:
                found = True
                break
            elif current.next == None:
                break
            
            prevNode = current
            current = current.getNext()
        
        if found:
            prevNode.next = current.getNext()
            return True

        print("Value does not exist in the Linked List")
        return False



    def deleteDLL(self):
        if self.head == None:
            print("Doubly Linked List is already empty")
        else:
            self.head = None
doublyLinkedList = DoublyLinkedList()

# Push Value to the beginining of DoublyLinkedList
newNode = Node(7)
doublyLinkedList.pushNode(newNode)
doublyLinkedList.pushValue(5)
doublyLinkedList.pushValue(3)

doublyLinkedList.insertAfter(newNode, 9)

# Append Value to the beginining of DoublyLinkedList
doublyLinkedList.append(11)
doublyLinkedList.append(13)

print("After Insertion: ", [node.value for node in doublyLinkedList])


doublyLinkedList.delete(9)
doublyLinkedList.delete(7)

print("After Deletion: ", [node.value for node in doublyLinkedList])

# Search for value in DoublyLinkedList
print("Searching For 13, Found: ", doublyLinkedList.search(13).value)
print("Searching For 99, Found: ", doublyLinkedList.search(99))


print("SIZE OF LINKEDLIST IS: ", doublyLinkedList.size())

doublyLinkedList.deleteDLL()
print("After Deleting Doubly LinkedList: ", [node.value for node in doublyLinkedList])