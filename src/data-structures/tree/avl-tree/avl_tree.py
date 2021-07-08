from queue import *

class AVLNode:
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1

def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

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

def searchNode(rootNode, nodeValue):
    if rootNode.data == nodeValue:
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



avlRoot = AVLNode(20)
