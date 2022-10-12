# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Solution 1
def sorted_list_to_bst(head):
    if not head: return head
    if not head.next: return TreeNode(head.val)

    slow = fast = head
    prev = None

    while fast and fast.next:
        prev = slow
        slow, fast = slow.next, fast.next.next
    
    prev.next =  None

    left = sorted_list_to_bst(head)
    right = sorted_list_to_bst(slow.next)

    return TreeNode(slow.val, left, right)




# Solution 2
def sorted_list_to_bst_2(head):
    data, node = [], head
    while node:
        data.append(node.val)
        node = node.next
    
    def buildTree(start, end):
        if start >= end: return
        mid = (start + end) // 2

        left = buildTree(start, mid)
        right = buildTree(mid + 1, end)

        return TreeNode(data[mid], left, right)
    
    return buildTree(0, len(data))