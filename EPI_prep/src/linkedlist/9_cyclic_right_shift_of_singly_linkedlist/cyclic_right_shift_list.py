class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next

# Time O(n) | Space O(1)
def cyclic_right_shift_list(L, k):
    if not L:
        return L
        
    tail, list_length = L, 1
    while tail.next:
        tail = tail.next
        list_length += 1
    
    # make list circular
    k =  k % list_length
    if k == 0:
        return L
    
    # makes list a cycle by connecting the tail to the head
    tail.next = L
    new_tail = L
    for _ in range(k - 1):
        new_tail = new_tail.next
    
    new_head, new_tail.next= new_tail.next, None
    return new_head
    

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


# Before Befor Shift
print_node(l1_2)

# Shift List By 2
new_list = cyclic_right_shift_list(l1_2, 3)
print_node(new_list) # [9, 11, 2, 5, 7]

# Shift List By 1
print_node(cyclic_right_shift_list(new_list, 1)) # [11, 2, 5, 7, 9]