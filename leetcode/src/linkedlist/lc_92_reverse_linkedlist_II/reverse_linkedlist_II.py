# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseBetween(head, left, right):
    if not head and not head.next: return head
    prev, curr = None, head

    i = 1
    while curr and i < left:
        prev, curr = curr, curr.next
        i += 1
    
    last_node_after_reverse, node_before_reverse = curr, prev
    i = 0
    while curr and i < right - left + 1:
        next_node = curr.next
        curr.next = prev
        prev, curr = curr, next_node
        i += 1
    
    if node_before_reverse:
        node_before_reverse.next = prev
    else:
        head = prev
    
    last_node_after_reverse.next = curr

    return head