from __future__ import print_function

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

# Space complexity O(N/K), 
# If we have an array of length 6 and K = 3, 
# Our function will call itself twice since we have to K elements during one function call
# Hence space complexity will be O(N/K)

def reverse_every_k_elements(head, k):
    if k <= 1 or head is None:
        return head
    
    prev, current = None, head
    return reverse_sub_list(head, prev, current, k)

def reverse_sub_list(head, prev, current, k):
    last_node_of_prev_part = prev
    last_node_of_sublist = current
    i = 0
    next = None
    
    while current is not None and i < k:
        next = current.next
        current.next = prev
        prev = current
        current = next
        i += 1

    if last_node_of_prev_part is not None:
        last_node_of_prev_part.next = prev
    else:
        head = prev
    
    last_node_of_sublist.next = current
    
    if current is None:
        return head
    
    prev = last_node_of_sublist
    
    return reverse_sub_list(head, prev, current, k)

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = Node(7)
head.next.next.next.next.next.next.next = Node(8)

print("Nodes of original LinkedList are: ", end='')
head.print_list()
result = reverse_every_k_elements(head, 3)
print("Nodes of reversed LinkedList are: ", end='')
result.print_list()









