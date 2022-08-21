class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val, self.next, self.prev = val, next, prev


# Time O(n + m) | Space O(1)
# where n and m are the lengths of each of the two input lists.
def merge_two_sorted_lists(A, B):
    sentinel = iter = ListNode(0)

    while A and B:
        if A.val < B.val:
            iter.next, A.prev = A, iter
            A = A.next
        else:
            iter.next, B.prev = B, iter
            B = B.next
        
        iter = iter.next
    
    iter.next = A or B
    return sentinel.next



l1_2 = ListNode(2)
l1_5 = ListNode(5)
l1_7 = ListNode(7)
l1_2.next, l1_5.prev, l1_5.next = l1_5, l1_2, l1_7

l2_3 = ListNode(3)
l2_11 = ListNode(11)
l2_3.next, l2_11.prev = l2_11, l2_3

result = merge_two_sorted_lists(l1_2, l2_3) # [2,3,5,7,11]

while result:
    print(result.val, end=" ")
    result = result.next