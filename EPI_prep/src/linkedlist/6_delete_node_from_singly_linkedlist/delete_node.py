class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next

# Time O(1) | Space O(1)
# assumes node is not the tail
def delete_node(node_to_be_deleted):
    node_to_be_deleted.val = node_to_be_deleted.next.val
    node_to_be_deleted.next = node_to_be_deleted.next.next

l1_2 = ListNode(2)
l1_5 = ListNode(5)
l1_7 = ListNode(7)
l1_9 = ListNode(9)
l1_2.next, l1_5.next = l1_5, l1_7
l1_7.next = l1_9


def print_node(node):
    while node:
        print(node.val, end=" ")
        node = node.next
    
    print("\n")


print_node(l1_2) 

delete_node(l1_7)
print_node(l1_2) 

delete_node(l1_5)
print_node(l1_2) 