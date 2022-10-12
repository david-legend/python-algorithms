def getIntersectionNode(headA, headB):
    if not headA or not headB: return
    A_count, B_count = count_list(headA), count_list(headB)

    if B_count > A_count:
        headA, headB = headB, headA

    i = 0
    while i < abs(A_count - B_count):
        headA = headA.next
        i += 1
    
    while headA and headB and headA != headB:
        headA, headB = headA.next, headB.next
    
    return headA
    

def count_list(node):
    count = 0
    while node:
        node = node.next
        count += 1
    
    return count