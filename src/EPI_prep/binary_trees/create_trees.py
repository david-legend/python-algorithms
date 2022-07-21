class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def deserialize(self, data):
        nodes = data.split(",")
        self.i = 0
        
        def dfs():
            if nodes[self.i] == "X":
                self.i += 1
                return None
            
            node = TreeNode(int(nodes[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            
            return node
        
        return dfs()

codec = Codec()
test_1 = codec.deserialize("4,-4,-2,X,7,1,X,X,6")
print(test_1)