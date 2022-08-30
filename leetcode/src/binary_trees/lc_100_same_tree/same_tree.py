class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


def same_tree(p, q):
    def same_tree_helper(nodeP, nodeQ):
        if nodeP is None and nodeQ is None:
            return True
        
        if nodeP is None or nodeQ is None:
            return False

        if nodeP.val !=  nodeQ.val:
            return False
            
        return same_tree_helper(nodeP.left, nodeQ.left) and same_tree_helper(nodeP.right, nodeQ.right)

    return same_tree_helper(p, q)



def same_tree_concise(p, q):
    def same_tree_helper(nodeP, nodeQ):
        if nodeP is None and nodeQ is None:
            return True
        elif nodeP and nodeQ:
            return nodeP.val == nodeQ.val and \
                same_tree_helper(nodeP.left, nodeQ.left) and \
                same_tree_helper(nodeP.right, nodeQ.right)
        
        return False

    return same_tree_helper(p, q)