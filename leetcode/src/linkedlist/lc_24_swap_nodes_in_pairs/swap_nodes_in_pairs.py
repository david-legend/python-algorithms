def swapPairs(head):
    if not head or not head.next: return head

    prev, curr = None, head
    while curr:
        last_node_previous_sublist, last_node_of_sublist = prev, curr
        i = 2
        while curr and i > 0:
            next_node = curr.next
            curr.next = prev
            prev, curr = curr, next_node
            i -= 1
        
        if last_node_previous_sublist is None:
            head = prev
        else:
            last_node_previous_sublist.next = prev

        last_node_of_sublist.next = curr
        prev = last_node_of_sublist
    return head