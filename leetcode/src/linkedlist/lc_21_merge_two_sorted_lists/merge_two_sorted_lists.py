# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Time complexity: O(m + n)
# where m and n represents the length of the two list nodes

# Space complexity: O(1)    
def mergeTwoLists(list1, list2):
    sentinel = merge = ListNode(0)
    while list1 and list2:
        if list1.val < list2.val:
            merge.next, list1 = list1, list1.next
        else:
            merge.next, list2 = list2, list2.next
        merge = merge.next
    
    merge.next = list1 or list2
    return sentinel.next