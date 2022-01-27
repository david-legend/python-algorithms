class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Time complexity
# The time complexity of the algorithm is O(N^2)
# ​​in the worst case, where ‘N’ is the total number of nodes in the tree. 
# This is due to the fact that we traverse each node once, but for every node, we iterate the current path. 
# The current path, in the worst case, can be O(N)O(N) (in the case of a skewed tree). 
# But, if the tree is balanced, then the current path will be equal to the height of the tree, i.e., O(logN). 
# So the best case of our algorithm will be O(NlogN).

# Space complexity
# The space complexity of the algorithm will be O(N). 
# This space will be used to store the recursion stack. T
# he worst case will happen when the given tree is a linked list (i.e., every node has only one child). 
# We also need O(N) space for storing the currentPath in the worst case.
# Overall space complexity of our algorithm is O(N).

def count_paths(root, S):
    return count_paths_recurse(root, S, [])

def count_paths_recurse(curr_node, S, current_path):
    if curr_node is None:
        return 0
    
    current_path.append(curr_node.val)
    path_count, path_sum = 0, 0
    
    for i in range(len(current_path) -1, -1, -1):
        path_sum += current_path[i]
        
        if path_sum == S:
            path_count += 1
            
    path_count += count_paths_recurse(curr_node.left, S, current_path)
    path_count += count_paths_recurse(curr_node.right, S, current_path)
    
    del current_path[-1]
    
    return path_count

root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(4)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
print("Tree has paths: " + str(count_paths(root, 11)))


