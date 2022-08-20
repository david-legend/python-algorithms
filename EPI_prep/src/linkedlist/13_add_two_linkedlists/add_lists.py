

class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next

# Time O(n + m) | Space O(max(n, m))
# where n and m are the lengths of the two lists.
def add_list(L1, L2):
    result = result_iter = ListNode(0)
    carry = 0

    while L1 or L2 or carry:
        sum = carry + (L1.val if L1 else 0) + (L2.val if L2 else 0)
        result_iter.next = ListNode(sum % 10)
        carry = sum // 10
        L1 = L1.next if L1 else None
        L2 = L2.next if L2 else None
        result_iter = result_iter.next
    
    return result.next

head1 = ListNode(3)
node_1 = ListNode(1)
node_2 = ListNode(4)
head1.next, node_1.next = node_1, node_2

head2 = ListNode(7)
node_3 = ListNode(0)
node_4 = ListNode(9)
head2.next, node_3.next = node_3, node_4


def print_node(node):
    while node:
        print(node.val, end="")
        node = node.next
    
    print("\n")



# add 413 + 907 = 1320  --> 0231
print_node(add_list(head1, head2)) # 0231

node_4.next = ListNode(7)

# add 413 + 7907 = 8320  --> 0238
print_node(add_list(head1, head2)) # 0238