# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def splitListToParts(head, k):
    curr, list_length = head, 0
    while curr:
        curr = curr.next
        list_length += 1

    min_split_count, remainder = divmod(list_length, k)
    result, curr = [], head
    for i in range(k):
        partition_head = partition = ListNode(None)
        extra = int(i < remainder)

        for j in range(min_split_count + extra):
            partition.next = partition = ListNode(curr.val)
            if curr: 
                curr = curr.next

        result.append(partition_head.next)
    
    return result