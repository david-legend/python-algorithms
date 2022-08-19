class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next

# Time O(n) | Space O(1)
def remove_duplicates(L):
    it = L
    while it:
        # Uses next-distinct to find the next distinct value.
        next_distinct = it.next
        while next_distinct and next_distinct.val == it.val:
            next_distinct = next_distinct.next
        it.next = next_distinct
        it = next_distinct

    return L

l1_2 = ListNode(2)
l1_5 = ListNode(5)
l1_5_dup = ListNode(5)
l1_9 = ListNode(9)
l1_9_dup = ListNode(9)
l1_2.next, l1_5.next = l1_5, l1_5_dup
l1_5_dup.next, l1_9.next = l1_9, l1_9_dup


def print_node(node):
    while node:
        print(node.val, end=" ")
        node = node.next
    
    print("\n")


# Before Removing Duplicates
print_node(l1_2)

print_node(remove_duplicates(l1_2)) # [2, 5, 9]
