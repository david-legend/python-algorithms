class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next

# Time O(n) | Space O(1)
def add_list(L1, l2):
    pass

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



print_node(add_list(head1, head2)) # 1320

node_4.next = ListNode(7)


print_node(add_list(head1, head2)) # 1320