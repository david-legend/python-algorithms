from collections import deque

class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val, self.next = val, None
        self.left, self.right = left, right 

def compute_right_sibling_tree(tree):
    if tree:
        queue = deque([tree])
        while queue:
            level_size = len(queue)
            node = None
            for _ in range(level_size):
                curr = queue.popleft()
                if node:
                    node.next = curr
                    node = node.next
                else:
                    node = curr

                if curr.left:
                    queue.append(curr.left)

                if curr.right:
                    queue.append(curr.right)




node_1 = TreeNode(1)
node_2 = TreeNode(2)
node_3 = TreeNode(3)
node_4 = TreeNode(4)
node_5 = TreeNode(5)
node_6 = TreeNode(6)
node_7 = TreeNode(7)

node_1.left, node_1.right = node_2, node_3
node_2.left, node_2.right = node_4, node_5
node_3.left, node_3.right = node_6, node_7

print(compute_right_sibling_tree(node_1))