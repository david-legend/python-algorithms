class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next

# Time O(n) | Space O(1)
def isPalindrome(L):
    pass

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


def print_node(node):
    while node:
        print(node.val, end=" ")
        node = node.next
    
    print("\n")



print_node(isPalindrome(head)) # True
node_4.val = 19

print_node(isPalindrome(head)) # False
print_node(isPalindrome(ListNode(16))) # True