class Node:
    def __init__(self, val):
        self.val, self.next = val, None

def print_list(node):
    if node:
        while node is not None:
            print(node.val)
            node = node.next

def reverse_list(node):
    if node is None or node.next is None:
        return node
    
    p = reverse_list(node.next)
    node.next.next = node
    node.next = None

    return p

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

print("Before reversing list")
print_list(n1)

reverse_list(n1)

print("\nAfter reversing list")
print_list(n5) # n5 becomes the new head