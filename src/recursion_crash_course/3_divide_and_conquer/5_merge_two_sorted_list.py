class Node:
    def __init__(self, val):
        self.val, self.next = val, None


def printList(node):
    if node:
        curr_node = node
        while curr_node:
            print(curr_node.val)
            curr_node = curr_node.next

def merge(A, B):
    if A is None: return B
    if B is None: return A

    if A.val <= B.val:
        A.next = merge(A.next, B)
        return A
    else:
        B.next = merge(A, B.next)
        return B


n1 = Node(2)
n1.next = Node(7)
n1.next.next = Node(12)
n1.next.next.next = Node(15)

n2 = Node(5)
n2.next = Node(6)
n2.next.next = Node(14)
n2.next.next.next = Node(18)

printList(merge(n1, n2))