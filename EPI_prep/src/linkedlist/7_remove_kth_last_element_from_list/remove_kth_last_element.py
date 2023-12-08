class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next

# Time O(n) | Space O(1)
# Assumes L has at least k nodes, deletes the k-th last node in L.
def delete_kth_last_node(L, k):
    if L:
        dummy_head = fast = ListNode(0, L)
        for _ in range(k):
            fast = fast.next

        slow = dummy_head
        while fast.next and slow.next:
            fast, slow = fast.next, slow.next
        
        slow.next = slow.next.next

        return dummy_head.next

# Time O(n) | Space O(1)
# Assumes L has at least k nodes, deletes the k-th last node in L.
def delete_kth_last_node_2(L, k):
    if not L or (not L.next and k == 1): return None
    if k == 0: return L

    dummy_head = ListNode(0, L)
    it = slow = fast = dummy_head

    count = 0
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        count += 1
    list_length = count * 2 if fast else (count * 2) - 1
    
    for _ in range(list_length - k):
        it = it.next
    
    it.next = it.next.next
    return dummy_head.next

l1_2 = ListNode(2)
l1_5 = ListNode(5)
l1_7 = ListNode(7)
l1_9 = ListNode(9)
l1_11 = ListNode(11)
l1_2.next, l1_5.next = l1_5, l1_7
l1_7.next, l1_9.next = l1_9, l1_11


def print_node(node):
    while node:
        print(node.val, end=" ")
        node = node.next
    
    print("\n")


# Before Deletion
print_node(l1_2)

# Deleting node 3rd node from behind  - 7
print_node(delete_kth_last_node(l1_2, 3)) # [2, 5, 9, 11]

# Deleting node 2nd node from behind - 9
print_node(delete_kth_last_node(l1_2, 2)) # [2, 5,  11]

# Deleting node 1st node from behind - 11
print_node(delete_kth_last_node(l1_2, 1)) # [2, 5,  11]

# Deleting node 2nd node from behind (head) - 2
print_node(delete_kth_last_node(l1_2, 2)) # [2, 5,  11]



l1_2 = ListNode(2)
l1_5 = ListNode(5)
l1_7 = ListNode(7)
l1_9 = ListNode(9)
l1_11 = ListNode(11)
l1_2.next, l1_5.next = l1_5, l1_7
l1_7.next, l1_9.next = l1_9, l1_11

print("\n\nSolution 2")
# Before Deletion
print_node(l1_2)

# Deleting node 3rd node from behind  - 7
print_node(delete_kth_last_node_2(l1_2, 3)) # [2, 5, 9, 11]

# Deleting node 2nd node from behind - 9
print_node(delete_kth_last_node_2(l1_2, 2)) # [2, 5,  11]

# Deleting node 1st node from behind - 11
print_node(delete_kth_last_node_2(l1_2, 1)) # [2, 5,  11]

# Deleting node 2nd node from behind (head) - 2
print_node(delete_kth_last_node_2(l1_2, 2)) # [2, 5,  11]
