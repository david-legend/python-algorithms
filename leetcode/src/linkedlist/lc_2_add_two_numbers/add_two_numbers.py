# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
def addTwoNumbers(l1, l2):
    sentinel = result = ListNode(0)
    remainder = 0
    while l1 or l2 or remainder:
        l1_val = l1.val if l1 else 0
        l2_val = l2.val if l2 else 0
        
        curr_sum = l1_val + l2_val + remainder
        sentinel.next = ListNode(curr_sum % 10)
        remainder = curr_sum // 10

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
        sentinel = sentinel.next
    
    return result.next