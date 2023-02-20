from collections import deque, defaultdict
class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


def bottomView(root):
    if not root: return

    vertical_order = defaultdict(dict)
    queue = deque([(root, 0, 0)])

    while queue:
        level_size = len(queue)
        for _ in range(level_size):
            node, x, y = queue.popleft()

            if x not in vertical_order:
                vertical_order[x] = defaultdict(list)
            vertical_order[x][y].append(node.val)

            if node.left:
                queue.append((node.left, x-1, y+1))
            if node.right: 
                queue.append((node.right, x+1, y+1))

    result = []
    for key in sorted(vertical_order.keys()):
        val_keys = sorted(vertical_order[key].keys())
        bottom_view_key = val_keys[-1]
        result.append(vertical_order[key][bottom_view_key].pop())
    
    return result



node1 = Node(20)
node2 = Node(8)
node3 = Node(22)
node4 = Node(5)
node5 = Node(3)
node6 = Node(4)
node7 = Node(25)
node8 = Node(10)
node9 = Node(14)

node1.left, node1.right = node2, node3
node2.left, node2.right = node4, node5
node3.right = node7
node5.left, node5.right = node8, node9

print(bottomView(node1)) #[5, 10, 3, 14, 25]

node3.left = node6
node5.right = None
node6.right = node9

print(bottomView(node1)) #[5, 10, 4, 14, 25]