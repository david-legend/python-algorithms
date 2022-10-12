# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Time O(n) | Space O(1)
def oddEvenList(head):
    if not head: return head
    even_head = even_it = ListNode()
    odd_head = odd_it = ListNode()
    node, i = head, 1
    while node:
        if i % 2 == 0:
            even_it.next = node 
            even_it = even_it.next
        else:
            odd_it.next = node
            odd_it = odd_it.next
        i += 1
        node = node.next
    
    even_it.next, odd_it.next = None, even_head.next
    return odd_head.next