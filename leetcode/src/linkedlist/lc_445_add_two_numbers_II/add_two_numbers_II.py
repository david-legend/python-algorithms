# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    sentinel = result = ListNode(0)
    l1, l2 = reverse(l1), reverse(l2)
    carry = 0

    while l1 or l2 or carry:
        l1_val = l1.val if l1 else 0
        l2_val = l2.val if l2 else 0
        curr_sum = l1_val + l2_val + carry

        result.next = ListNode(curr_sum % 10)
        # update carry 
        carry = curr_sum // 10
        # update pointers 
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
        result = result.next
    
    return reverse(sentinel.next)


def reverse(node):
    curr, prev = node, None
    while curr:
        next_node = curr.next
        curr.next = prev
        prev, curr = curr, next_node

    return prev