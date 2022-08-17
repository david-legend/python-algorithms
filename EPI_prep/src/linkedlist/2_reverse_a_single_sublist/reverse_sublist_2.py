
class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next


# Time O(n) | Space O(1) 
def reverse_sublist(A, s, f):
    prev_node, curr_node = None, A

    i = 1
    while curr_node and i != s:
        prev_node = curr_node
        curr_node = curr_node.next
        i += 1
    
    node_before_s, node_at_f_after_reversal = prev_node, curr_node
    
    i = 0
    while curr_node and f - s + 1 != i:
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node
        i += 1
    
    if node_before_s is None:
        A = prev_node
    else:
        node_before_s.next = prev_node
    
    node_at_f_after_reversal.next = curr_node
    return A

    



l1_2 = ListNode(2)
l1_3 = ListNode(3)
l1_5 = ListNode(5)
l1_7 = ListNode(7)
l1_11 = ListNode(11)
l1_2.next, l1_3.next = l1_3, l1_5
l1_5.next, l1_7.next = l1_7, l1_11


result = reverse_sublist(l1_2, 2, 4) # [2,3,5,7,11]

while result:
    print(result.val, end=" ")
    result = result.next