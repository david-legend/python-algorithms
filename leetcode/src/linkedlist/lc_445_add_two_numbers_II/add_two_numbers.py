# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    l1_stack, l2_stack = create_stack(l1), create_stack(l2)
    carry, result = 0, None

    while l1_stack or l2_stack or carry:
        l1_val = l1_stack.pop() if l1_stack else 0
        l2_val = l2_stack.pop() if l2_stack else 0
        curr_sum = l1_val + l2_val + carry

        carry = curr_sum // 10
        tmp, result = result, ListNode(curr_sum % 10)
        result.next = tmp
        
    return result

def create_stack(node):
    curr, stack = node, []
    while curr:
        stack.append(curr.val)
        curr = curr.next

    return stack