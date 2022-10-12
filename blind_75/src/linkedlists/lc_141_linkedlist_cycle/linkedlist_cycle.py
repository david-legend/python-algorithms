def has_cycle(head):
    if not head: return False

    slow = fast = head
    while fast.next and fast.next.next:
        slow, fast = slow.next, fast.next.next
        if slow == fast:
            return True
    
    return False