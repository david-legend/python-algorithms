from queue import *
class TreeNode:
    # Creation of tree
    # Runtime complexity O(1) Space Complexity O(1)
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.leftChild = None
        self.rightChild = None


# Traversing a tree using preOrderTraversal
# Run time complexity O(n) & 
# Space Complexity O(n) --> because we are using recursion, function calls are kept on the stack
def preOrderTraversal(rootNode):
    if not rootNode:
        return
    
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)


# Traversing a tree using inOrderTraversal
# Run time complexity O(n) & 
# Space Complexity O(n) --> because we are using recursion, function calls are kept on the stack
def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

# Traversing a tree using postOrderTraversal
# Run time complexity O(n) & 
# Space Complexity O(n) --> because we are using recursion, function calls are kept on the stack
def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

# Traversing a tree using levelOrderTraversal
# Run time complexity O(n) & Space Complexity O(n)
def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        queue = Queue()
        queue.enqueue(rootNode)

        while not(queue.isEmpty()):
            root = queue.dequeue()
            print(root.value.data)

            if (root.value.leftChild is not None):
                queue.enqueue(root.value.leftChild)

            if (root.value.rightChild is not None):
                queue.enqueue(root.value.rightChild)

# Searching a binary tree using levelOrderTraversal
# Run time complexity O(n) & Space Complexity O(n)
def searchBinaryTree(rootNode, value):
    if not rootNode:
        return
    else:
        queue = Queue()
        queue.enqueue(rootNode)
        
        while not(queue.isEmpty()):
            root = queue.dequeue()

            if (root.value.data == value):
                return root.value.data

            if root.value.leftChild is not None:
                queue.enqueue(root.value.leftChild)

            if root.value.rightChild is not None:
                queue.enqueue(root.value.rightChild)

        return None

def insertNode(rootNode, newNode):
    if not rootNode:
        rootNode = newNode
        return rootNode
    else:
        queue = Queue()
        queue.enqueue(rootNode)

        while not(queue.isEmpty()):
            root = queue.dequeue()

            if(root.value.leftChild is not None):
                queue.enqueue(root.value.leftChild)
            else:
                root.value.leftChild = newNode
                return root.value.leftChild

            if(root.value.rightChild is not None):
                queue.enqueue(root.value.rightChild)
            else:
                root.value.rightChild = newNode
                return root.value.rightChild


def getDeepestNode(rootNode):
    if not rootNode:
        return
    else:
        queue = Queue()
        queue.enqueue(rootNode)

        while not(queue.isEmpty()):
            root = queue.dequeue()

            if(root.value.leftChild is not None):
                queue.enqueue(root.value.leftChild)

            if(root.value.rightChild is not None):
                queue.enqueue(root.value.rightChild)   
        deepestNode = root.value
        return deepestNode


def deleteDeepestNode(rootNode, deepestNode):
    if not rootNode:
        return
    else:
        queue = Queue()
        queue.enqueue(rootNode)

        while not(queue.isEmpty()):
            root = queue.dequeue()

            if root is deepestNode:
                root.value = None
                return True

            if(root.value.leftChild is not None):
                if root.value.leftChild is deepestNode:
                    root.value.leftChild = None
                    return True
                else:
                    queue.enqueue(root.value.leftChild)
           

            if(root.value.rightChild is not None):
                if root.value.rightChild is deepestNode:
                    root.value.rightChild = None
                    return True
                else:
                    queue.enqueue(root.value.rightChild)
                
        return False

# Deleting a node in binary tree
# Run time complexity O(n) & Space Complexity O(n)
def deleteNode(rootNode, value):
    if not rootNode:
        return
    else:
        queue = Queue()
        queue.enqueue(rootNode)

        while not(queue.isEmpty()):
            root = queue.dequeue()

            if root.value.data == value:
                deepestNode = getDeepestNode(rootNode)
                root.value.data = deepestNode.data
                deleteDeepestNode(rootNode, deepestNode)
                return True

            if root.value.leftChild is not None:
                    queue.enqueue(root.value.leftChild)

            if root.value.rightChild is not None:
                    queue.enqueue(root.value.rightChild)
        
        return False

# Deleting entire binary tree
# Run time complexity O(1) & Space Complexity O(1)
def deleteBinaryTree(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return True


root = TreeNode("Drinks")
insertNode(root, TreeNode("Hot"))
insertNode(root, TreeNode("Cold"))
insertNode(root, TreeNode("Tea"))
insertNode(root, TreeNode("Coffee"))
insertNode(root, TreeNode("Beer"))
insertNode(root, TreeNode("Soda"))


print("--- PreOrder Traversal ---")
preOrderTraversal(root)
print("--- End PreOrder Traversal --- \n\n")

print("--- InOrder Traversal ---")
inOrderTraversal(root)
print("--- End of InOrder Traversal --- \n\n")

print("--- PostOrder Traversal ---")
postOrderTraversal(root)
print("--- End of PostOrder Traversal --- \n\n")

print("--- LevelOrder Traversal ---")
levelOrderTraversal(root)
print("--- End of LevelOrder Traversal --- \n\n")

print("Searching for Coffee, Found --> ", searchBinaryTree(root, "Coffee"))
print("Searching for Scotch, Found --> ", searchBinaryTree(root, "Scotch"), "\n\n")


print("--- Deleting Node with Value 'Cold' ---")
print("Delete Successful? ", deleteNode(root, "Cold"))
print("--- Printing Values after deletion ---")
levelOrderTraversal(root)
print("-------- \n\n")

print("--- Deleting Entire BinaryTree ---")
print("Deletion Successful? ", deleteBinaryTree(root))
print("--- Printing Values after deletion ---")
levelOrderTraversal(root)
print("--------\n\n")