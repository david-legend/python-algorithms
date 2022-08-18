
class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next


# Time O(f) | Space O(1) 
# where f is the position of the target destination
def reverse_sublist(A, s, f):
    dummy_head = sublist_head = ListNode(0, A)
    for _ in range(1, s):
        sublist_head = sublist_head.next
    
    sublist_iter = sublist_head.next
    for _ in range(f-s):
        next_node = sublist_iter.next
        # swap next node with predecessor node
        sublist_iter.next = next_node.next
        next_node.next = sublist_head.next
        # connect sublist_head back with the new swapped nodes
        sublist_head.next = next_node
    
    return dummy_head.next


    



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