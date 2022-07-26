class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    
#Time Complexity
#The time complexity of our algorithm will be O(N) 
#where ‘N’ is the total number of nodes in the LinkedList.

#Space Complexity
#The algorithm runs in constant space O(1).

def has_cycle(head):
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        
        if fast == slow:
            return True
    
    return False




head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
print("LinkedList has cycle: " + str(has_cycle(head)))

head.next.next.next.next.next.next = head.next.next
print("LinkedList has cycle: " + str(has_cycle(head)))

head.next.next.next.next.next.next = head.next.next.next
print("LinkedList has cycle: " + str(has_cycle(head)))