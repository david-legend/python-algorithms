# Time complexity
# The algorithm below has a time complexity of O(N)
# where ‘N’ is the number of nodes in the LinkedList.

# Space complexity
# The algorithm runs in constant space O(1).
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def is_palindromic_linked_list(head):
    if head is None or head.next is None:
        return True
    
    slow, fast = head, head
    
    while (fast is not None and fast.next is not None):
        slow = slow.next
        fast = fast.next.next
    
    head_second_half = reverse_list(slow)
    copy_head_second_half = head_second_half
    
    
    while head is not None and head_second_half is not None:
        if head.value != head_second_half.value:
            break
        head = head.next
        head_second_half = head_second_half.next
    
    reverse_list(copy_head_second_half)
    
    if head is None or head_second_half is None:
        return True
    
    return False
    
def reverse_list(head):
    prev = None
    while head:
        next = head.next
        head.next = prev
        prev = head
        head = next
        
    return prev



head = Node(2)
head.next = Node(4)
head.next.next = Node(6)
head.next.next.next = Node(4)
head.next.next.next.next = Node(2)

print("Is palindrome: " + str(is_palindromic_linked_list(head)))

head.next.next.next.next.next = Node(2)
print("Is palindrome: " + str(is_palindromic_linked_list(head)))

