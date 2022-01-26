# Time complexity
# The time complexity of the above algorithm is O(N^2), 
# where ‘N’ is the total number of nodes in the tree. T
# his is due to the fact that we traverse each node once (which will take O(N)), 
# and for every leaf node, we might have to store its path 
# (by making a copy of the current path) which will take O(N).

# Space complexity O(N*logN)
# If we ignore the space required for the allPaths list, 
# the space complexity of the above algorithm will be O(N) in the worst case. 
# This space will be used to store the recursion stack. 
# The worst-case will happen when the given tree is a linked list 
# (i.e., every node has only one child).

# Since, for binary trees, there exists only one path to reach any leaf node, 
# we can easily say that total root-to-leaf paths in a binary tree can’t be more 
# than the number of leaves. 
# As we know that there can’t be more than (N+1)/2 leaves in a binary tree, 
# therefore the maximum number of elements in allPaths will be O((N+1)/2) = O(N). 
# 
# Now, each of these paths can have many nodes in them. 
# For a balanced binary tree (like above), each leaf node will be at maximum depth. 
# As we know that the depth (or height) of a balanced binary tree is O(logN) we can say that, 
# at the most, each path can have logNlogN nodes in it. 
# This means that the total size of the allPaths list will be O(N*logN). 
# If the tree is not balanced, we will still have the same worst-case space complexity.

# From the above discussion, we can conclude that our algorithm’s overall space complexity is O(N*logN).
# Also, from the above discussion, since for each leaf node, 
# in the worst case, we have to copy log(N) nodes to store its path; 
# therefore, the time complexity of our algorithm will also be O(N*logN).

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_paths(root, sum):
    all_paths = []
    get_paths(root, sum, [], all_paths)
    
    return all_paths

def get_paths(root, sum, current_path, all_paths):
    if root is None:
        return
    
    # add the current node to the path
    current_path.append(root.val)
    
    # if the current node is a leaf and its value is equal to required_sum, save the current path
    if root.val == sum and root.left is None and root.right is None:
        all_paths.append(list(current_path))   
    else:
        # traverse the left sub-tree
        get_paths(root.left, sum - root.val, current_path, all_paths)
        # traverse the right sub-tree
        get_paths(root.right, sum - root.val, current_path, all_paths)
    
    # remove the current node from the path to backtrack,
    # we need to remove the current node while we are going up the recursive call stack.
    del current_path[-1]

root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(4)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
sum = 23
print("Tree paths with sum " + str(sum) +
    ": " + str(find_paths(root, sum)))


