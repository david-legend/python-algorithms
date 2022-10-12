# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Solution 1
def removeElements(head, val):
    if not head: return head
    sentinel = prev = ListNode(0, head)
    curr = head

    while curr:
        if curr.val == val:
            prev.next = curr.next
        else:
            prev = prev.next
        curr = curr.next
    
    return sentinel.next


# Solution 2
def removeElements2(head, val):
    if not head: return head
    curr = head
    sentinel = prev = ListNode()

    while curr:
        if curr.val != val:
            prev.next = ListNode(curr.val)
            prev = prev.next
        curr = curr.next
    
    return sentinel.next