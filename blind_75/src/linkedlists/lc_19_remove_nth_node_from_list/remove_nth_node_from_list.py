# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def removeNthFromEnd(head, n):
    sentinel = slow = ListNode(-1, head)
    fast = head

    while fast and n > 0:
        fast = fast.next
        n -= 1
    
    while fast:
        slow, fast = slow.next, fast.next
    
    slow.next = slow.next.next
    return sentinel.next