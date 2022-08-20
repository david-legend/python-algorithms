class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next

# Time O(n) | Space O(1)
def isPalindrome(L):
    if not L or L.next is None:
        return True

    slow = fast = L
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
    
    s1, s2 = reverse_linkedlist(slow), L
    while s1 and s2:
        if s1.val != s2.val:
            return False
        s1, s2 = s1.next, s2.next

    return True

def reverse_linkedlist(node):
    curr_node, prev_node = node, None
    while curr_node:
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node, curr_node = curr_node, next_node
    
    return prev_node

head = ListNode(1)
node_1 = ListNode(3)
node_2 = ListNode(5)
node_3 = ListNode(7)
node_4 = ListNode(5)
node_5 = ListNode(3)
node_6 = ListNode(1)
head.next, node_1.next = node_1, node_2
node_2.next, node_3.next = node_3, node_4
node_4.next, node_5.next = node_5, node_6


print(isPalindrome(head)) # True
node_4.val = 19

print(isPalindrome(head)) # False
print(isPalindrome(ListNode(16))) # True