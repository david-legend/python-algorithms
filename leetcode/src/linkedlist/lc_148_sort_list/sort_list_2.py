from heapq import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def sortList(head):
    if not head or not head.next: return head

    min_heap, curr = [], head
    while curr:
        heappush(min_heap, curr.val)
        curr = curr.next  
    
    sorted_list = result = ListNode(heappop(min_heap))

    while min_heap:
        next_node = ListNode(heappop(min_heap))
        result.next = next_node
        result = result.next
    
    return sorted_list


data = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
node = sortList(data)

while node:
    print(node.val, end=" ")
    node = node.next