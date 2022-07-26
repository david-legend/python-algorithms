class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time complexity #
# The time complexity of the algorithm is O(N), 
# where ‘N’ is the total number of nodes in the tree. 
# This is due to the fact that we traverse each node once.

# Space complexity
# The space complexity of the algorithm will be O(N) in the worst case. 
# This space will be used to store the recursion stack. 
# The worst case will happen when the given tree 
# is a linked list (i.e., every node has only one child).
class TreeDiameter:

    def __init__(self):
        self.treeDiameter = 0

    def find_diameter(self, root):
        self.calculate_height(root)
        return self.treeDiameter

    def calculate_height(self, currentNode):
        if currentNode is None:
            return 0

        leftTreeHeight = self.calculate_height(currentNode.left)
        rightTreeHeight = self.calculate_height(currentNode.right)

        # if the current node doesn't have a left or right subtree, we can't have
        # a path passing through it, since we need a leaf node on each side
        if leftTreeHeight is not None and rightTreeHeight is not None:

            # diameter at the current node will be equal to the height of left subtree +
            # the height of right sub-trees + '1' for the current node
            diameter = leftTreeHeight + rightTreeHeight + 1

            # update the global tree diameter
            self.treeDiameter = max(self.treeDiameter, diameter)

        # height of the current node will be equal to the maximum of the heights of
        # left or right subtrees plus '1' for the current node
        return max(leftTreeHeight, rightTreeHeight) + 1




treeDiameter = TreeDiameter()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.left = TreeNode(5)
root.right.right = TreeNode(6)
print("Tree Diameter: " + str(treeDiameter.find_diameter(root)))
root.left.left = None
root.right.left.left = TreeNode(7)
root.right.left.right = TreeNode(8)
root.right.right.left = TreeNode(9)
root.right.left.right.left = TreeNode(10)
root.right.right.left.left = TreeNode(11)
print("Tree Diameter: " + str(treeDiameter.find_diameter(root)))









