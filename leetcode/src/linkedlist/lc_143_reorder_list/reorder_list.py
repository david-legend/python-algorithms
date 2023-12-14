# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorderList(head) -> None:
    if not head or not head.next: return

    last_node_of_first_half, slow, fast = None, head, head
    while fast and fast.next:
        last_node_of_first_half = slow
        slow, fast = slow.next, fast.next.next

    last_node_of_first_half.next = None
    first_half, second_half = head, reverse(slow)

    while first_half and second_half:
        first_half_next_node = first_half.next
        second_half_next_node = second_half.next
        first_half.next, second_half.next = second_half, first_half.next

        if not first_half_next_node:
            second_half.next = second_half_next_node

        first_half, second_half = first_half_next_node, second_half_next_node


def reverse(node):
    prev, curr = None, node
    while curr:
        next_node = curr.next
        curr.next = prev
        prev, curr = curr, next_node
    
    return prev
    

def reorderList2(head) -> None:
    if not head and not head.next: return head
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
    
    head_of_first_half, head_of_second_half = head, reverse(slow)
    while head_of_first_half and head_of_second_half:
        next_head = head_of_first_half.next
        head_of_first_half.next = head_of_second_half
        head_of_first_half = next_head

        next_head = head_of_second_half.next
        head_of_second_half.next = head_of_first_half
        head_of_second_half = next_head

    if head_of_first_half:
        head_of_first_half.next = None

