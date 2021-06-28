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

#TODO:: Search, Delete, InsertAfter 
class CircularLinkedList:
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


    def printCLList(self):
        node = self.head
        while(node):
            print(node.value)
            if node.next == self.head:
                break
            node = node.getNext()


    # Function to insert a node at the beginning of a
    # circular linked list
    def push(self, value):
        node = Node(value)
        temp = self.head
         
        node.next = self.head
 
        # If linked list is not None (Meaning linkedList already contains at least one value)
        # If so move through the existing linked list till you find a node that has it's next value 
        # pointing back to the head (this is the last node)
        # When we do, set it to point to the new head
        if self.head is not None:
            while(temp.next != self.head):
                temp = temp.next
            #setting last node to point back to the new head
            temp.next = node
        # If it is an empty linked-list, set the new node to point to itself    
        else:
            node.next = node # For the first node
 
        # finally set the head of the linked-list to the new node
        self.head = node
            
    def append(self, value):
        node = Node(value)
        
        if self.head is None:
            self.head = node
            node.next = node
        else:
            current = self.head
            while current:
                if(current.next == self.head):
                    break
                else:
                    current = current.getNext()
            current.next = node
            node.next = self.head

    def size(self):
        current = self.head
        count = 0
        while current:
            if current.next == self.head:
                count += 1
                break;
            else:
                count += 1
                current = current.getNext()
        
        return count


linkedList = CircularLinkedList()
linkedList.push(3)
linkedList.push(2)
linkedList.push(1)
linkedList.append(4)

linkedList.printCLList()
print([node.value for node in linkedList])
