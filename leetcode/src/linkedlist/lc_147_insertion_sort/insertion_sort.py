# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



def insertionSortList(head):
    sentinel, curr = ListNode(), head

    while curr:
        prev = sentinel
        while prev.next and curr.val >= prev.next.val:
            prev = prev.next
        
        next_node = curr.next
        curr.next = prev.next
        prev.next = curr

        curr = next_node
    
    return sentinel.next