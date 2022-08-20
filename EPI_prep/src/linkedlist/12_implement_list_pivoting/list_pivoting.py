
class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next

# Time O(n) | Space O(1)
def list_pivot(L, x):
    if not L:
        return L
    
    left_head = left_node_it = ListNode(0)
    pivot_head = pivot_node_it = ListNode(0)
    right_head = right_node_it = ListNode(0)

    while L:
        if L.val < x:
            left_node_it.next = L
            left_node_it = left_node_it.next
        elif L.val == x:
            pivot_node_it.next = L
            pivot_node_it = pivot_node_it.next
        else:
            right_node_it.next = L
            right_node_it = right_node_it.next
        L = L.next

    right_node_it.next = None
    pivot_node_it.next = right_head.next
    left_node_it.next = pivot_head.next

    return left_head.next





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
print_node(list_pivot(ListNode(1), -100)) # [3,2,2,5,7,11,11]

