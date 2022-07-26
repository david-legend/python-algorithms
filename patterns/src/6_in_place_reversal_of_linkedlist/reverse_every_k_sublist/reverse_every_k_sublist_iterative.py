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

# Space complexity
# We only used constant space, therefore, 
# the space complexity of our algorithm is O(1).

def reverse_every_k_elements(head, k):
    if k <= 1 or head is None:
        return head
    
    previous, current = None, head
    while True:
        last_node_of_prev_part = previous
        last_node_sub_list = current
        
        i, next = 0, None
        while current is not None and i < k:
            next = current.next
            current.next = previous
            previous = current
            current = next
            i += 1
        
        if last_node_of_prev_part is not None:
            last_node_of_prev_part.next = previous
        else:
            head = previous
        
        last_node_sub_list.next = current
        
        if current is None:
            break
        previous = last_node_sub_list
        
    return head

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









