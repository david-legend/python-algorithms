# Time Complexity
# Finding the cycle in a LinkedList with ‘N’ nodes 
# and also finding the length of the cycle requires O(N). 
# We will need O(N) to find the start of the cycle. 
# Therefore, the overall time complexity of our algorithm will be O(N).

# Space Complexity
# The algorithm runs in constant space O(1).
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    

def find_cycle_start(head):
    slow, fast = head, head
    cycle_count = 0
    while (fast is not None and fast.next is not None):
        fast = fast.next.next
        slow = slow.next
        
        if slow == fast:
            cycle_count = calculate_cycle_count(slow)
            break
    
    return find_start(head, cycle_count)

def calculate_cycle_count(slow):
    current = slow
    cycle_count = 0
    
    while True:
        current = current.next
        cycle_count += 1
        
        if current == slow:
            break
    
    return cycle_count

def find_start(head, cycle_count):
    pointer_1 = head
    pointer_2 = head
    
    while cycle_count > 0:
        pointer_1 = pointer_1.next
        cycle_count -= 1
        
    while pointer_1 != pointer_2:
        pointer_1 = pointer_1.next
        pointer_2 = pointer_2.next
    
    return pointer_1


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)

print("LinkedList cycle start: " + str(find_cycle_start(head).value))

head.next.next.next.next.next.next = head.next.next
print("LinkedList cycle start: " + str(find_cycle_start(head).value))

head.next.next.next.next.next.next = head.next.next.next
print("LinkedList cycle start: " + str(find_cycle_start(head).value))

head.next.next.next.next.next.next = head
print("LinkedList cycle start: " + str(find_cycle_start(head).value))