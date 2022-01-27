class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Time complexity
# The time complexity of the above algorithm is O(N), 
# where ‘N’ is the total number of nodes in the tree. 
# This is due to the fact that we traverse each node once.

# Space complexity
# The space complexity of the above algorithm will be O(N) in the worst case. 
# This space will be used to store the recursion stack. 
# The worst case will happen when the given tree is a linked list (i.e., every node has only one child).

def find_path(root, sequence):
    if root is None:
        return len(sequence) == 0
    return check_sequence(root, sequence, 0)  

def check_sequence(root, sequence, idx):
    if root is None:
        return False
    
    sequence_len = len(sequence)
    if idx >= sequence_len or root.val != sequence[idx]:
        return False
    
    if root.left is None and root.right is None:
        return True
    
    return check_sequence(root.left, sequence, idx+1) or check_sequence(root.right, sequence, idx+1)


root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(1)
root.left.left = TreeNode(1)
root.right.left = TreeNode(6)
root.right.right = TreeNode(5)

print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))


