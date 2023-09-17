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
    

# Explanation:
# We know for a fact that if there is a cycle, the slow and fast pointers will meet at a point. (see linkedlist_cycle for explanation)
# but how do we know for a fact that if we move the slow pointer at pointer at step of 1 at the point where they collided and another pointer
# at the step of 1 from the head, they are bound to meet at the point where the cycle starts.
# this can be proven mathematically

# 
#               4 - 5 - 6
#             /           \
#   1 - 2 - 3             7
#             \          /
#              10 - 9 - 8
#
# lets label the distance from head to the start of cycle as L1 (ie. 1-2-3)
# lets label the distance travelled by slow pointer till collision with fast pointer as L1 + L2 (where l2 is distance travelled from start of cycle till collision)
# Then we can label distance travelled by fast  pointer as L1 + L2 + X -> since the fast pointer has travelled same distance as slow pointer and some more (x denotes the extra distance)

# S = L1 + L2 
# F = L1 + L2 + X
# if we want to equate the two formulas we have to multiply S by 2 because F has travelled twice its distance
# 2 (L1 + L2) =  L1 + L2 + X
# L1 + L2  = X
# then L1  = X - L2 
#

# if L2 is the distance from start of cycle to collision
# and X is the extra distance travelled by the fast pointer
# and its difference X - L2 = L1,
# this means that the distance travelled from collision to start of cycle will be the same as the distance from head to start of collision
# this explains the solution below

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