class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    
#Time Complexity
#The time complexity of our algorithm will be O(N) 
#where ‘N’ is the total number of nodes in the LinkedList.

#Space Complexity
#The algorithm runs in constant space O(1).


# Explanation:
# why is guaranteed that if a pointer (slow pointer) is moving at one step and another pointer(fast pointer) is moving at
# 2 steps, they are bound to colide
# this is because if it takes the slow pointer n steps to get to the tail, it will take the fast pointer n/2 steps to get to the tail
# hence the slow and fast pointers are bound to be meet when the fast pointer travels n steps. 
#  
#  Example::
#
#  -------------------
#  0  1  2  3  4  5  6
#  
#  if we take the number line above and we plot the n steps for both the slow and fast pointer --> (where n steps is the steps it takes to reach the end of the line for the slow pointer)
#  after plotting we see that they collide at a point. (in this example n = 6)
#  Even though in this example we used the starting point as the begining of the cycle, this gives us an assurance that no matter where the cycle begins at some point the fast and slow pointer 
#  will collide

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