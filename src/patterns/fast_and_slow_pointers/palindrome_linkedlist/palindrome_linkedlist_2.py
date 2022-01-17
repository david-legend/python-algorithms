import math

# Time complexity
# The algorithm below has a time complexity of O(N)
# where ‘N’ is the number of nodes in the LinkedList.

# Space complexity
# The algorithm runs in constant space O(1).
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    
# Solution 2
def is_palindromic_linked_list_2(head):
    if head is None or head.next is None:
        return True

    count = 0 #length of linkedlist
    head_start = 0 #to move pointer to middle of linkedlist
    start, middle = head, head
    curr_node = head

    #get length of linkedlist
    while curr_node:
        count += 1
        curr_node = curr_node.next

    #decide center of linkedlist based on length
    if count % 2 == 0:
        head_start = count/2
    else:
        head_start = math.ceil(count/2)

    step = 0
    # move middle pointer to the center of linkedlist
    while step != head_start-1:
        step += 1
        middle = middle.next

    sum_1 = 0
    sum_2 = 0
    # sum from start to middle and from middle to end
    while middle is not None and start is not None:
        sum_1 += start.value
        sum_2 += middle.value
        start = start.next
        middle = middle.next

    # isPalindrome is sums are equal
    return sum_1 == sum_2



# Testing Solution 2
root = Node(2)
root.next = Node(4)
root.next.next = Node(6)
root.next.next.next = Node(6)
root.next.next.next.next = Node(4)
root.next.next.next.next.next = Node(2)

print("Is palindrome: " + str(is_palindromic_linked_list_2(root)))

root.next.next.next.next.next.next = Node(2)
print("Is palindrome: " + str(is_palindromic_linked_list_2(root)))