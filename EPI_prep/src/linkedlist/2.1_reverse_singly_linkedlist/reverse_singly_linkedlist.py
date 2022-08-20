class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next

# Time O(n) | Space O(1)
def reverse_linkedlist(L):
    prev_node, curr_node = None, L
    while curr_node:
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node, curr_node = curr_node, next_node
    
    return prev_node

head = ListNode(3)
node_1 = ListNode(1)
node_2 = ListNode(4)
head.next, node_1.next = node_1, node_2



def print_node(node):
    while node:
        print(node.val, end="")
        node = node.next
    
    print("\n")


print("Before Reverse : ")
print_node(head)

print("After Reverse : ")
print_node(reverse_linkedlist(head)) # 413