
class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next


# Time O(n) | Space O(1) 
def reverse_sublist(head, k):
    if k <= 1:
        return head

    prev, curr_node = None, head
    while curr_node:
        node_before_reversal, node_after_reversal = prev, curr_node

        i = 0
        while curr_node and i != k:
            next_node = curr_node.next
            curr_node.next = prev
            prev, curr_node = curr_node, next_node
            i += 1
        
        if node_before_reversal is None:
            head = prev
        else:
            node_before_reversal.next = prev
        
        node_after_reversal.next = curr_node
        prev = node_after_reversal
    
    return head




head = ListNode(1)
l1_2 = ListNode(2)
l1_3 = ListNode(3)
l1_4 = ListNode(4)
l1_5 = ListNode(5)
l1_6 = ListNode(6)
head.next, l1_2.next = l1_2, l1_3
l1_3.next, l1_4.next = l1_4, l1_5
l1_5.next = l1_6

def print_node(head):
    node = head
    while node:
        print(node.val, end=" ")
        node = node.next
    print("\n")


print("before reversing every k sublist\n")
print_node(head)

result = reverse_sublist(head, 2) # [2,1,4,3,6,5]
print_node(result)


