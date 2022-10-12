# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def rotateRight(head, k):
    if not head: return head
    list_length, tail = 1, head
    while tail.next:
        tail = tail.next
        list_length += 1
    
    # make list circular list
    tail.next = head
    k = k % list_length
    rotation_count = list_length - k - 1
    new_tail = head
    for _ in range(rotation_count):
        new_tail = new_tail.next
    
    head, new_tail.next = new_tail.next, None
    return head



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