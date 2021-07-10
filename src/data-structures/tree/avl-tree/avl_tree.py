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


def getHeight(rootNode):
    if not rootNode:
        return 0
    return rootNode.height

# Compare the simple examples below to the code to get better understanding
# Example 1 -> Left left imbalance
# supposed we have a tree like this:
#       (5)
#      /
#    (4) 
#    /
#  (2) 
# newRoot =  (4)
#           /
#         (2)  
# disbalancedNode.leftChild = None  -->  #  (5)
#                                          /
#                                       None
# newRoot =  (4)
#           /  \
#         (2)  (5) 

# Example 2 -> Right left imbalance
# supposed we have a tree like this: The disbalanced node we first pass in would be (4)
#       (5)
#         \
#        (4)  
#        /
#      (2) 
# newRoot =  (2) 
# disbalancedNode.leftChild = None  -->  #  (2)
#                                          /
#                                       None
# newRoot =  (2)
#           /  \
#         None  (4)                         
def rightRotate(disbalancedNode):
    newRoot = disbalancedNode.leftChild
    disbalancedNode.leftChild = disbalancedNode.leftChild.rightChild
    newRoot.rightChild = disbalancedNode
    # compute the new heights for disbalancedNode and newRoot
    disbalancedNode.height = 1 + max(getHeight(disbalancedNode.leftChild), getHeight(disbalancedNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(disbalancedNode.rightChild))
    return newRoot

# Compare the simple examples below to the code to get better understanding
# Example 1 -> Right Right imbalance
# supposed we have a tree like this:
#       (5)
#         \
#        (4) 
#          \
#         (2) 
# newRoot =  (4)
#              \
#             (2)
# disbalancedNode.rightChild = None  -->  # (5)
#                                             \
#                                            None
# newRoot =  (4)
#           /  \
#         (5)  (2)

# Example 2 -> Left Right imbalance
# supposed we have a tree like this: The disbalanced node we first pass in would be (4)
#       (5)
#       /
#     (4)  
#       \
#      (2) 
# newRoot =  (2)        
# disbalancedNode.rightChild = None  -->   (4)
#                                           \  
#                                           (2)
#                                           /
#                                        None
# newRoot =  (2)
#           /  \
#         (4)  None   
def leftRotate(disbalancedNode):
    newRoot = disbalancedNode.rightChild
    disbalancedNode.rightChild = disbalancedNode.rightChild.leftChild
    newRoot.leftChild = disbalancedNode
    disbalancedNode.height = 1 + max(getHeight(disbalancedNode.leftChild), getHeight(disbalancedNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(disbalancedNode.rightChild))
    return newRoot

def getBalance(rootNode):
    if not rootNode:
        return
    return getHeight(rootNode.leftChild) - getHeight(rootNode.rightChild)

def insertNode(rootNode, nodeValue):
    if not rootNode:
        return AVLNode(nodeValue)
    elif nodeValue < rootNode.data:
        rootNode.leftChild = insertNode(rootNode.leftChild, nodeValue)
    else:
        rootNode.rightChild = insertNode(rootNode.rightChild, nodeValue)
    
    rootNode.height = 1 + max(getHeight(rootNode.leftChild), getHeight(rootNode.rightChild))
    balance = getBalance(rootNode)

    # Left Left Condition
    if balance > 1 and nodeValue < rootNode.leftChild.data:
        return rightRotate(rootNode)
    # Left Right Condition
    if balance > 1 and nodeValue > rootNode.leftChild.data:
        rootNode.leftChild = leftRotate(rootNode.leftChild)
        return rightRotate(rootNode)
    # Right Right Condition
    if balance < -1 and nodeValue > rootNode.rightChild.data:
        return leftRotate(rootNode)
    # Right Left Condition
    if balance < -1 and nodeValue < rootNode.rightChild.data:
        rootNode.rightChild = rightRotate(rootNode.rightChild)
        return leftRotate(rootNode)
    return rootNode

def getMinValueNode(rootNode):
    if rootNode is None or rootNode.leftChild is None:
        return rootNode
    return getMinValueNode(rootNode.leftChild)

def deleteNode(rootNode, nodeValue):
    if not rootNode:
        return rootNode
    elif nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        elif rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp
        temp = getMinValueNode(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)
    balance = getBalance(rootNode)

    if balance > 1 and getBalance(rootNode.leftChild) >= 0:
        return rightRotate(rootNode)
    if balance < -1 and getBalance(rootNode.rightChild) <= 0:
        return leftRotate(rootNode)
    if balance > 1 and getBalance(rootNode.leftChild) < 0:
        rootNode.leftChild = leftRotate(rootNode.leftChild)
        return rightRotate(rootNode)
    if balance < -1 and getBalance(rootNode.rightChild) > 0:
        rootNode.rightChild = rightRotate(rootNode.rightChild)
        return leftRotate(rootNode)
    
    return rootNode


def deleteAVL(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "AVL Tree Deleted"

# Insertion For a binary search tree, this is how the tree would look like after insertion
#    (5)
#       \
#      (10)
#        \
#       (15)
#         \
#        (20)

# But for an AVL tree, this is how the tree would look like 
# after insertion (increasing the time needed to traverse the tree)
#    (10)
#     / \
#   (5) (15) 
#        \
#       (20)

avlRoot = AVLNode(5)
avlRoot = insertNode(avlRoot, 10)
avlRoot = insertNode(avlRoot, 15)
avlRoot = insertNode(avlRoot, 20)

print("--- Level Order Traversal After Insert---")
levelOrderTraversal(avlRoot)
print("\n\n")

# deleting node
print("--- Deleting Node with Value '20' ---")
deleteNode(avlRoot, 20)
print("--- Printing Values after deletion ---")
levelOrderTraversal(avlRoot)
print("-------- \n\n")



# deleting entire tree
print("--- Deleting Entire AVL Tree ---")
deleteAVL(avlRoot)
print("--- Printing Values after deletion ---")
levelOrderTraversal(avlRoot)
print("--------\n\n")



