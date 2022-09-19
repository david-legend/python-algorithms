# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        """
        def preorder(node):
            if node is None: return result.append("x")
            
            result.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
            
        
        result = []
        preorder(root)
        
        return ",".join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        """
        def deserializeHelper():
            nonlocal index
            if not nodes or index >= len(nodes) or nodes[index] == "x": 
                index += 1
                return None
            
            node_val = nodes[index]
            index += 1
            left = deserializeHelper()
            right = deserializeHelper()
            
            curr_node = TreeNode(node_val)
            curr_node.left, curr_node.right = left, right
            return curr_node
        
        nodes, index = data.split(","), 0
        print(nodes)
        return deserializeHelper()