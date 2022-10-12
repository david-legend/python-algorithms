from unittest.mock import sentinel


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Solution 1
# Time O(n) | Space O(1)
def deleteDuplicates(head):
    node = new_head = head
    while node:
        it = node.next
        while it and it.val == node.val:
            it = it.next
        
        node.next = it
        node = node.next
    
    return new_head



# Solution 2
# Time O(n) | Space O(1)
def deleteDuplicates2(head):
    sentinel = result = ListNode(0)
    node = head

    while node:
        it = node.next
        while it and it.val == node.val:
            it = it.next
        
        result.next = node
        result, node = result.next, it
    
    result.next = None
    return sentinel.next