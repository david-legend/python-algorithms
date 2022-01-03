from queue import *

class BinarySearchTree:
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.leftChild = None
        self.rightChild = None

def insertNode(rootNode, nodeValue):
    if rootNode.data == None:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BinarySearchTree(nodeValue)
        else:
            insertNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BinarySearchTree(nodeValue)
        else:
            insertNode(rootNode.rightChild, nodeValue)
    print("Value inserted")
    return True

# Traversing a tree using preOrderTraversal
# Run time complexity O(n) & Space Complexity O(n)
def preOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        print(rootNode.data)
        preOrderTraversal(rootNode.leftChild)
        preOrderTraversal(rootNode.rightChild)

# Traversing a tree using inOrderTraversal
# Run time complexity O(n) & Space Complexity O(n)
def inOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        inOrderTraversal(rootNode.leftChild)
        print(rootNode.data)
        inOrderTraversal(rootNode.rightChild)

# Traversing a tree using postOrderTraversal
# Run time complexity O(n) & Space Complexity O(n)
def postOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
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
            
            if root.value.leftChild is not None:
                queue.enqueue(root.value.leftChild)

            if root.value.rightChild is not None:
                queue.enqueue(root.value.rightChild)



def searchNode(rootNode, nodeValue):
    if not rootNode:
        return

    if rootNode.data == nodeValue:
        print("Value Found", rootNode.data)
        return rootNode.data
    elif nodeValue < rootNode.data:
        if rootNode.data == nodeValue:
            print("Value Found")
            return rootNode.data
        else:
            searchNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.data == nodeValue:
            print("Value Found")
            return rootNode.data
        else:
            searchNode(rootNode.rightChild, nodeValue)


def getMinValueNode(node):
    current = node
    while current.leftChild is not None:
        current = current.leftChild
    return current

def deleteNode(rootNode, nodeValue):
    if rootNode is None:
        return rootNode
    if nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        
        if rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp
        
        temp = getMinValueNode(rootNode.rightChild)
        rootNode.data = temp.data 
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)
    return rootNode

# Deleting entire binary search tree
# Run time complexity O(1) & Space Complexity O(1)
def deleteBinaryTree(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return True
      


root = BinarySearchTree(78)
insertNode(root, 64)
insertNode(root, 96)
insertNode(root, 45)
insertNode(root, 89)
insertNode(root, 140)
insertNode(root, 311)
insertNode(root, 599)
insertNode(root, 11)

print("\n\n")
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

print("Searching for 311, Found --> ", searchNode(root, 311))
print("Searching for 599, Found --> ", searchNode(root, 599), "\n\n" )


print("--- Deleting Node with Value '96' ---")
print("Delete Successful? ", deleteNode(root, 96))
print("--- Printing Values after deletion ---")
levelOrderTraversal(root)
print("-------- \n\n")

print("--- Deleting Entire Binary Search Tree ---")
print("Deletion Successful? ", deleteBinaryTree(root))
print("--- Printing Values after deletion ---")
levelOrderTraversal(root)
print("--------\n\n")