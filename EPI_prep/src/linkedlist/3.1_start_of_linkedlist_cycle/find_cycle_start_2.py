
class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next


def find_cycle_start(head):
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next

        if slow is fast:
            slow = head

            while slow is not fast:
                slow, fast = slow.next, fast.next
            
            return slow




l1_2 = ListNode(2)
l1_3 = ListNode(3)
l1_5 = ListNode(5)
l1_7 = ListNode(7)
l1_11 = ListNode(11)
l1_2.next, l1_3.next = l1_3, l1_5
l1_5.next, l1_7.next = l1_7, l1_3


print(find_cycle_start(l1_2).val) # 3

