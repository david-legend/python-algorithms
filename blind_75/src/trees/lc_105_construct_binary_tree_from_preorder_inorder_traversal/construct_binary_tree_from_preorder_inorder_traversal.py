class TreeNode:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left, self.right = left, right

def construct_tree(preorder, inorder):
    inorder_val_to_idx = {data: i for i, data in enumerate(inorder)}

    def construct_tree_helper(po_start, po_end, io_start, io_end):
        if po_start >= po_end or io_start >= io_end: return

        node_val = preorder[po_start]
        inorder_root_idx = inorder_val_to_idx[node_val]  
        subtree_size = inorder_root_idx - io_start

        po_start += 1
        po_left_end = po_start + subtree_size
        left = construct_tree_helper(po_start, po_left_end, io_start, inorder_root_idx)
        right = construct_tree_helper(po_left_end, po_end, inorder_root_idx+1, io_end)

        return TreeNode(node_val, left, right)
    return construct_tree_helper(0, len(preorder), 0, len(inorder))