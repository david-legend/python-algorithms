# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Solution 1
# Time O(1) | Space O(1)


# Goal : delete node 2.
		
# 1  ->   2 -> 3       -> 4
#         ^    ^
#         |    |
#        node  node.next

#     #step one:  change the node value to 3
#     1  ->  3   3           4
#         ^    ^           ^
#         |    |           |
#         node  node.next   node.next.next
        
#     #step two: change the next pointer to point to node.next.next
#     1  ->  3   ->          4
#         ^    ^           ^
#         |    |           |
#         node  node.next   node.next.next
# Result    
# 1 ->3 ->4
def deleteNode(node):
    node.val = node.next.val
    node.next = node.next.next



# Solution 2
# Time O(n) | Space O(1)
def deleteNode(node):
    while node:
        node.val = node.next.val
        if node.next and node.next.next is None:
            node.next = None
        
        node = node.next