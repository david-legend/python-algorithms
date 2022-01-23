from __future__ import print_function

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        count = 0
        while temp is not None and count < 8:
            print(temp.value, end=" ")
            temp = temp.next
            count += 1
        print()


def reverse_sub_list(head, p, q):
    if p == q:
        return head

    current, previous = head, None
    i = 0
    
    while current is not None and i < p - 1:
        previous = current
        current = current.next
        i += 1
    
    node_before_p = previous
    node_at_position_p = current
    
    next = None
    i = 0
    while current is not None and i < q - p + 1:
        next = current.next
        current.next = previous
        previous = current
        current = next
        i += 1
    
    if node_before_p is not None:
        node_before_p.next = previous
    else:
        head = previous
    
    node_at_position_p.next = current 
    return head

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)


print("Nodes of original LinkedList are: ", end='')
head.print_list()
result = reverse_sub_list(head, 2, 4)
print("Nodes of reversed LinkedList are: ", end='')
result.print_list()



