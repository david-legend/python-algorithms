# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        def preorder(node):
            if node is None: 
                result.append('x')
                return
            
            result.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
        
        result = []
        preorder(root)
        
        return ",".join(result)
            
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        data =  data.split(",")
        
        def deserializeHelper():
            nonlocal node_idx
            
            if data[node_idx] == 'x':
                node_idx += 1
                return None
            
            node_val = int(data[node_idx])
            node_idx += 1
            left = deserializeHelper()
            right = deserializeHelper()
            
            return TreeNode(node_val, left, right)
        
        node_idx = 0
        return deserializeHelper()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))