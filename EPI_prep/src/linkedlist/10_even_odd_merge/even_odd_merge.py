class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next

# Time O(n) | Space O(1)
def even_odd_merge(L):
    pass

head = ListNode(0)
node_1 = ListNode(1)
node_2 = ListNode(2)
node_3 = ListNode(3)
node_4 = ListNode(4)
node_5 = ListNode(5)
node_6 = ListNode(6)
head.next, node_1.next = node_1, node_2
node_2.next, node_3.next = node_3, node_4
node_4.next, node_5.next = node_5, node_6


def print_node(node):
    while node:
        print(node.val, end=" ")
        node = node.next
    
    print("\n")


# Before Before Merge
print_node(head)

# After Merge
print_node(even_odd_merge(head)) # [0,2,4,6,1,3,5]
