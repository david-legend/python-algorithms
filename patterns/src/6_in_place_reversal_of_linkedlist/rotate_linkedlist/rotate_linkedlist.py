from __future__ import print_function
from unittest import skip

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()


# Time complexity
# The time complexity of our algorithm will be O(N) 
# where ‘N’ is the total number of nodes in the LinkedList.

# Space complexity
# We only used constant space, therefore, 
# the space complexity of our algorithm is O(1).

def rotate(head, k):
    if k == 0 or head is None or head.next is None:
        return head
    
    list_length = 1
    last_node = head
    
    while last_node.next is not None:
        last_node = last_node.next
        list_length += 1
    
    
    
    rotations = k % list_length
    if rotations == 0: 
        return head

    last_node.next = head
    skip_length = list_length - rotations - 1
    last_node_of_rotated_list = head
    for _ in range(skip_length):
        last_node_of_rotated_list = last_node_of_rotated_list.next
    
    head = last_node_of_rotated_list.next
    last_node_of_rotated_list.next = None
    
    return head


def solution2(head, k):
    if k == 0 or not head or not head.next: return head
    list_length, tail = 1, head
    while tail.next:
        tail = tail.next
        list_length += 1
    
    rotations = k % list_length
    if rotations == 0: return head
    
    it, i = head, 0
    while it and i < list_length - rotations - 1:
        i += 1
        it = it.next

    new_tail, new_head = it, it.next

    tail.next, new_tail.next = head, None
    return new_head


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)

print("Solution 1")
print("Nodes of original LinkedList are: ", end='')
head.print_list()
result = rotate(head, 20)
print("Nodes of rotated LinkedList are: ", end='')
result.print_list()



head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)

print("\nSolution 2")
print("Nodes of original LinkedList are: ", end='')
head.print_list()
result = solution2(head, 20)
print("Nodes of rotated LinkedList are: ", end='')
result.print_list()

