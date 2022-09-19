from collections import namedtuple


def lca(root, p, q):
    Data = namedtuple('Data', ['ancestor', 'count'])
    def lca_helper(node):
        if node is None: return Data(None, 0)

        left = lca_helper(node.left)
        if left.count == 2:
            return left

        right = lca_helper(node.right)
        if right.count == 2:
            return right
        
        num_target_nodes = left.count + right.count + int(node is p) + int(node is q)
        return Data(node if num_target_nodes == 2 else None, num_target_nodes)

    return lca_helper(root).ancestor