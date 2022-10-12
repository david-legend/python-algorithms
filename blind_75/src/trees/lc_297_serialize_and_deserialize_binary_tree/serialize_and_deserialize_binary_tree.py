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
        def serialize_helper(node):
            if not node: 
                result.append("x")
                return
                
            result.append(str(node.val))
            serialize_helper(node.left)
            serialize_helper(node.right)

        result = []
        serialize_helper(root)

        return ",".join(result)
            

    def deserialize(self, data):
        data, i = data.split(","), 0

        def deserialize_helper():
            nonlocal i
            if data[i] == 'x':
                i += 1
                return None
            
            node_val = int(data[i])
            i += 1
            left = deserialize_helper()
            right = deserialize_helper()

            return  TreeNode(node_val, left, right)
        
        deserialize_helper()