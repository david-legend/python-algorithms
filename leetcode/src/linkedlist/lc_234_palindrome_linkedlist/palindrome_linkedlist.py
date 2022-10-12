# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head):
    if not head or not head.next: return True
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
    
    first_half, second_half = head, reverse_list(slow)
    while first_half and second_half:
        if first_half.val != second_half.val:
            return False
        first_half, second_half = first_half.next, second_half.next
    
    return True


def reverse_list(node):
    curr, prev = node, None
    while curr:
        next_node = curr.next
        curr.next = prev
        prev, curr = curr, next_node
    
    return prev