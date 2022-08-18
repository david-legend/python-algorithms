
class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next


def has_cycle(L):
    slow = fast = L

    while fast and fast.next:
        slow, fast = slow.next, fast.next.next

        if slow == fast:
            return True
    

l1_2 = ListNode(2)
l1_3 = ListNode(3)
l1_5 = ListNode(5)
l1_7 = ListNode(7)
l1_11 = ListNode(11)
l1_2.next, l1_3.next = l1_3, l1_5
l1_5.next, l1_7.next = l1_7, l1_3


print(has_cycle(l1_2)) # True

l1_7.next = l1_11

print(has_cycle(l1_2)) # None
