# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def detectCycle(head):
    slow = fast = head
    
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow == fast:
            pointer = head
            while pointer and slow and pointer != slow:
                slow, pointer = slow.next, pointer.next
            
            return pointer