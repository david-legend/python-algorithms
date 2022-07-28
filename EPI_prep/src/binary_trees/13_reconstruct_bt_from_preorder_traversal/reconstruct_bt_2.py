class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time O(n) | Space O(n)

def reconstruct(data):
    i = 0
    def construct():
        nonlocal i
        if data[i] == None:
            i += 1
            return None
        
        root = TreeNode(data[i])
        i += 1
        root.left = construct()
        root.right = construct()

        return root
    
    return construct()


node_1 = TreeNode(1)
node_2 = TreeNode(2)
node_3 = TreeNode(3)
node_4 = TreeNode(4)
node_5 = TreeNode(5)
node_6 = TreeNode(6)
node_7 = TreeNode(7)

node_1.left, node_1.right = node_2, node_3
node_2.left, node_2.right = node_4, node_5
node_3.left, node_3.right = node_6, node_7

tree = reconstruct([1, 2, 4, None, None, 5, None, None, 3, 6, None, None, 7, None, None])

def preorder_traversal(node):
    result = []
    def preorder(node):
        if node is None:
            return

        result.append(node.val)
        preorder(node.left)
        preorder(node.right)
    
    preorder(node)
    return result


print(preorder_traversal(tree)) # [1, 2, 4, 5, 3, 6, 7]