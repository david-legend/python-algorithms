# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def partition(head, x):
    head_of_values_before_target = before_target_it = ListNode(0)
    head_of_values_after_target = after_target_it = ListNode(0)
    it = head
    while it:
        if it.val < x:
            before_target_it.next = it
            before_target_it = before_target_it.next
        else:
            after_target_it.next = it
            after_target_it = after_target_it.next
        it = it.next
    
    after_target_it.next = None
    before_target_it.next = head_of_values_after_target.next
    return head_of_values_before_target.next