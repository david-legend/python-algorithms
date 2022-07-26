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
            
    def swap_nodes(self, key_1, key_2):
        if key_1 == key_2:
            return
        
        prev_1 = None
        curr_1 = self.head
        
        while curr_1 and curr_1.value != key_1:
            prev_1 = curr_1
            curr_1 = curr_1.next
            
        prev_2 = None
        curr_2 = self.head

        while curr_2 and curr_2.value != key_2:
            prev_2 = curr_2
            curr_2 = curr_2.next
            
        if not curr_1 or not curr_2:
            return
        
        if prev_1:
            prev_1.next = curr_2
        else:
            self.head = curr_2
            
        if prev_2:
            prev_2.next = curr_1
        else:
            self.head = curr_1
            
        curr_1.next, curr_2.next = curr_2.next, curr_1.next
     
     
    # the goal is to reverse 
    # a linkedlist like: A->B->C->D->NONE 
    # into D->C->B->A->None
    def reverse_iterative(self):
        prev = None
        curr = self.head
        while curr:
            # iter1: next = B->C->D->None
            # iter2: next = C->D->None 
            # iter3: next = D->None 
            # iter4: next = None 
            next = curr.next
            # iter1: curr.next = A->None
            # iter2: curr.next = B->A->None 
            # iter3: curr.next = C->B->A->None
            # iter4: curr.next = D->C->B->A->None
            curr.next = prev
            # iter1: prev = A->None
            # iter2: prev = B->A->None 
            # iter3: prev = C->B->A->None
            # iter4: prev = D->C->B->A->None
            prev = curr
            # iter1: curr = B->C->D->None
            # iter2: curr = C->D->None 
            # iter3: curr = D->None 
            # iter4: curr = None 
            curr = next
        
        # head = D->C->B->A->None
        self.head = prev
            
    def reverse_recursive(self):
        
        def _reverse_recursive(curr, prev):
            if not curr:
                return prev
            
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            
            return _reverse_recursive(curr, prev)
        
        self.head = _reverse_recursive(curr=self.head, prev=None)  
            
    def deleteLinkedList(self):
        self.head = None

linkedList = LinkedList()

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


# test swapping nodes 

llist = LinkedList()

llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")


print("Original List")
llist.printSLList()
print("\n\n")


llist.swap_nodes("B", "C")
print("Swapping nodes B and C that are not head nodes")
llist.printSLList()
print("\n\n")

llist.swap_nodes("A", "B")
print("Swapping nodes A and B where key_1 is head node")
llist.printSLList()
print("\n\n")

llist.swap_nodes("D", "B")
print("Swapping nodes D and B where key_2 is head node")
llist.printSLList()
print("\n\n")

llist.swap_nodes("C", "C")
print("Swapping nodes C and C where both keys are same")
llist.printSLList()
print("\n\n")