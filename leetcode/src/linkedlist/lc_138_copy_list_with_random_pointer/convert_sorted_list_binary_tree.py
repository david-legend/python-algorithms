class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

def copyRandomList(head):
    clone = {None: None}
    node = head
    while node:
        clone[node] = Node(node.val)
        node = node.next
    
    node = head
    while node:
        copy = clone[node]
        copy.next, copy.random = clone[node.next], clone[node.random]
        node = node.next

    return clone[head]