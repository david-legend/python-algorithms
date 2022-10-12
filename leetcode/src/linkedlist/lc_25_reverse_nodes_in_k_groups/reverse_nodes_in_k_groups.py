# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseKGroup( head, k):
    if not head or not head.next: return head

    list_length, node = 0, head
    while node:
        node = node.next
        list_length += 1

    prev, curr = None, head
    while curr and list_length >= k:
        last_node_previous_sublist, last_node_of_sublist = prev, curr
        i = k
        while curr and i > 0:
            next_node = curr.next
            curr.next = prev
            prev, curr = curr, next_node
            i -= 1
        
        if last_node_previous_sublist:
            last_node_previous_sublist.next = prev
        else:
            head = prev
        last_node_of_sublist.next = curr
        prev = last_node_of_sublist
        list_length -= k

    return head