# Solution 1
# Time O(n) | Space O(n)
def flatten(root):
    def flatten_helper(node):
        if node is None: return

        left = flatten_helper(node.left)
        right = flatten_helper(node.right)

        if left:
            curr_left = left
            while curr_left.right:
                curr_left = curr_left.right
            curr_left.right = right
        else:
            left = right

        node.right, node.left = left, None
        return node


    flatten_helper(root)




# Solution 2
# Time O(n) | Space O(n)
def flatten(root):
    def flatten_helper(node):
        if node is None: return

        left = flatten_helper(node.left)
        right = flatten_helper(node.right)

        if left:
            left.right = node.right
            node.right, node.left = node.left, None

        tail = right or left or node
        return tail
    
    flatten_helper(root)
