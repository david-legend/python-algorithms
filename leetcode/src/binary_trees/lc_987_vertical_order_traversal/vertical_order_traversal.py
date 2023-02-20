from sortedcontainers import SortedDict 
from collections import deque, defaultdict

# Solution 1
def verticalTraversal(root):
    if not root: return []

    position_map = defaultdict(list)
    queue = deque([(root, 0, 0)])
    
    while queue:
        level_size = len(queue)
        for _ in range(level_size):
            node, pos, depth = queue.popleft()
            position_map[(pos,depth)].append(node.val)
            if node.left: 
                queue.append((node.left, pos-1, depth+1))
            if node.right:
                queue.append((node.right, pos+1, depth+1))
        
        
    vertical_order = defaultdict(list)
    
    for key in sorted(position_map.keys()):
        pos, depth = key
        position_map[key].sort()
        vertical_order[pos].extend(position_map[key])

    return vertical_order.values()















# Solution 2
def verticalTraversal(root):
    if not root: return []

    queue = deque([(root, 0, 0)])
    sorted_levels = SortedDict()

    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node, x, y = queue.popleft()
            if x not in sorted_levels:
                sorted_levels.setdefault(x, SortedDict())
                sorted_levels[x].setdefault(y, [])
                sorted_levels[x][y].append(node.val)
            else:
                if y not in sorted_levels[x]:
                    sorted_levels[x].setdefault(y, [])
                sorted_levels[x][y].append(node.val)

            if node.left:
                queue.append((node.left, x-1, y+1))
                    
            if node.right:
                queue.append((node.right, x+1, y+1))
    
    result = []
    for levels in sorted_levels.values():
        vertical_level = []
        for arr in levels.values():
            arr.sort()
            vertical_level += arr
        result.append(vertical_level)

    return result