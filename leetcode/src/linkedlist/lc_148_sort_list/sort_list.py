# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def sortList(head):
    if not head or not head.next: return head

    mid = getMid(head)
    second_half = mid.next 
    mid.next = None

    left = sortList(head)
    right = sortList(second_half)

    return mergeTwoLists(left, right)

    
def getMid(head):
    slow = fast = head
    while fast.next and fast.next.next:
        slow, fast = slow.next, fast.next.next
    
    return slow

def mergeTwoLists(l1, l2):
    sentinel = merge = ListNode()
    while l1 and l2:
        if l1.val < l2.val:
            merge.next, l1 = l1, l1.next
        else:
            merge.next, l2 = l2, l2.next
        merge = merge.next

    merge.next = l1 or l2
    return sentinel.next


data = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
node = sortList(data)

while node:
    print(node.val, end=" ")
    node = node.next