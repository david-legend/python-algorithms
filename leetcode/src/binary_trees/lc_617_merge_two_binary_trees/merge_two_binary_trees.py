class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def merge_trees(root1, root2):
    def mergeTreesHelper(node1, node2):
        if node1 is None and node2 is None:
            return
        
        new_node_val = 0
        if node1 and node2:
            new_node_val = node1.val + node2.val
        
        if node1 or node2:
            new_node_val = (node1.val if node1 else 0) + (node2.val if node2 else 0)
        
        left = mergeTreesHelper(node1.left if node1 else None, node2.left if node2 else None)
        right = mergeTreesHelper(node1.right if node1 else None, node2.right  if node2 else None)
        
        return TreeNode(new_node_val, left, right)
    
    return mergeTreesHelper(root1, root2)