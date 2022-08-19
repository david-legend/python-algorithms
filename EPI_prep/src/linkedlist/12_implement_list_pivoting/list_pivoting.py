
class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next

# Time O(n) | Space O(1)
def list_pivot(L, x):
    pass

head = ListNode(3)
node_1 = ListNode(2)
node_2 = ListNode(2)
node_3 = ListNode(11)
node_4 = ListNode(7)
node_5 = ListNode(5)
node_6 = ListNode(11)
head.next, node_1.next = node_1, node_2
node_2.next, node_3.next = node_3, node_4
node_4.next, node_5.next = node_5, node_6


def print_node(node):
    while node:
        print(node.val, end=" ")
        node = node.next
    
    print("\n")


# Before Pivoting
print_node(head)

# After Merge
print_node(list_pivot(head, 7)) # [3,2,2,5,7,11,11]

