class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next

# Time O(n) | Space O(1)
def has_overlapping_lists(L1, L2):
    L1_length, l2_length = list_length(L1), list_length(L2)

    if l2_length > L1_length:
        L1, L2 = L2, L1

    for _ in range(abs(L1_length - l2_length)):
        L1 = L1.next
    
    while L1 and L2 and L1 is not L2:
        L1, L2 = L1.next, L2.next
    
    return L1

def list_length(head):
    curr_node = head
    length = 1
    while curr_node:
        curr_node = curr_node.next
        length += 1
    
    return length

l1_2 = ListNode(2)
l1_5 = ListNode(5)
l1_7 = ListNode(7)
l1_9 = ListNode(9)
l1_2.next, l1_5.next = l1_5, l1_7
l1_7.next = l1_9

l2_3 = ListNode(3)
l2_11 = ListNode(11)
l2_3.next, l2_11.next = l2_11, l1_7

print(has_overlapping_lists(l1_2, l2_3).val) #