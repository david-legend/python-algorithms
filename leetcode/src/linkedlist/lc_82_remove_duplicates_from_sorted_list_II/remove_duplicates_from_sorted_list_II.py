# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(head):
    sentinel = result = ListNode(0)
    node = head
    while node:
        it, is_duplicate = node.next, False
        while it and it.val == node.val:
            is_duplicate = True
            it = it.next
        
        if not is_duplicate:
            result.next = node
            result = result.next
        node = it

    result.next  = None
    return sentinel.next