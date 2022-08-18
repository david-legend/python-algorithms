
class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next


def find_cycle_start(head):
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next

        if slow is fast:
            cycle_count = cycle_length(slow)
            pointer_advanced = head
            for _ in range(cycle_count):
                pointer_advanced = pointer_advanced.next

            pointer_start = head
            while pointer_start is not pointer_advanced:
                pointer_start, pointer_advanced = pointer_start.next, pointer_advanced.next
            
            return pointer_start

def cycle_length(end):
    start = end
    cycle_count = 0
    while start:
        cycle_count += 1
        start = start.next
        if start is end:
            break

    return cycle_count



l1_2 = ListNode(2)
l1_3 = ListNode(3)
l1_5 = ListNode(5)
l1_7 = ListNode(7)
l1_11 = ListNode(11)
l1_2.next, l1_3.next = l1_3, l1_5
l1_5.next, l1_7.next = l1_7, l1_3


print(find_cycle_start(l1_2).val) # 3

