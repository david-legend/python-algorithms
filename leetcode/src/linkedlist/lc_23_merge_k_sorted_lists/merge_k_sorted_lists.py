from heapq import *
from unittest.mock import sentinel
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __lt__(self, other):
        return self.val < other.val

# Solution 1 - if not allowed to modify the ListNode Class

# Time - O (n log(k))
# where k is the number list nodes and m+n represents how long it takes to merge two list nodes

# Space: O(log(k))
def mergeKLists(lists):
    if len(lists) == 0: return
    while len(lists) > 1:
        result, list_length = [], len(lists)
        for i in range(0, list_length, 2):
            l1 = lists[i]
            l2 = lists[i+1] if i + 1 < list_length else None
            result.append(mergeTwoLists(l1, l2))
        lists = result

    return lists[0]

def mergeTwoLists(l1, l2):
    sentinel = merge = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            merge.next, l1 = l1, l1.next
        else:
            merge.next, l2 = l2, l2.next
        merge = merge.next
    
    merge.next = l1 or l2
    return sentinel.next



# Solution 2 - Overriding less than operator and using Min Heap
# Time complexity
# Since we’ll be going through all the elements of all arrays and 
# will be removing/adding one element to the heap in each step, 
# the time complexity of the above algorithm will be O(N*logK), 
# where ‘N’ is the total number of elements in all the ‘K’ input arrays.

# Space complexity
# The space complexity will be O(K) because, at any time, 
# our min-heap will be storing one number from all the ‘K’ input arrays.
def mergeKLists2(lists):
    min_heap = []
    for node in lists:
        heappush(min_heap, node)
    
    sentinel = merge = ListNode(0)
    while min_heap:
        curr = heappop(min_heap)
        merge.next, curr = curr, curr.next
        merge = merge.next

        if curr:
            heappush(min_heap, curr)
    
    return sentinel.next

l1 = ListNode(1, ListNode(2, ListNode(8)))
l2 = ListNode(3, ListNode(4, ListNode(7)))
l3 = ListNode(0, ListNode(6, ListNode(18)))


def print_list(node):
    while node:
        print(node.val, end=" ")
        node = node.next

print_list(mergeKLists2([l1, l2, l3]))