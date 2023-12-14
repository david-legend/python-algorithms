# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def rotateRight(head, k):
    if k == 0 or not head or not head.next: return head
    list_length, tail = 1, head
    while tail.next:
        tail = tail.next
        list_length += 1
    
    rotations = k % list_length
    if rotations == 0: return head
    
    it, i = head, 0
    while it and i < list_length - rotations - 1:
        i += 1
        it = it.next

    new_tail, new_head = it, it.next

    tail.next, new_tail.next = head, None
    return new_head



# Rotating Left Solution
def rotateLeft(head, k):
    if not head: return head
    list_length, tail = 1, head
    while tail.next:
        tail = tail.next
        list_length += 1
    
    # make list circular list
    tail.next = head
    rotation_count = (k % list_length) - 1
    new_tail = head
    for _ in range(rotation_count):
        new_tail = new_tail.next
    
    head, new_tail.next = new_tail.next, None
    return head