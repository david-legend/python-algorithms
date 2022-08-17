class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next


# Solution: 
# A naive approach is to append the two lists together and sort the resulting list.
#  The drawback of this approach is that it does not use the fact that the initial lists are sorted. 
# The time complexity is that of sorting, which is O((n + m)log(n + m)), where n and m are the lengths of each of the two input lists.

# Optimal Solution:
# A better approach, in terms of time complexity, is to traverse the two lists, always 
# choosing the node containing the smaller key to continue traversing from.


# Time O(n + m) | Space O(1)
# where n and m are the lengths of each of the two input lists.
def merge_two_sorted_lists(A, B):
    sentinel = it = ListNode(0)

    while A and B:
        if A.val < B.val:
            it.next, A = A, A.next
        else:
            it.next, B = B, B.next
        
        it = it.next
    
    it.next = A or B
    return sentinel.next



l1_2 = ListNode(2)
l1_5 = ListNode(5)
l1_7 = ListNode(7)
l1_2.next, l1_5.next = l1_5, l1_7

l2_3 = ListNode(3)
l2_11 = ListNode(11)
l2_3.next = l2_11

result = merge_two_sorted_lists(l1_2, l2_3) # [2,3,5,7,11]

while result:
    print(result.val, end=" ")
    result = result.next