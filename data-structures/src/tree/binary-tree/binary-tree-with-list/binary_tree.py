class BinaryTree:
    # Creation of tree
    # Runtime complexity O(1) Space Complexity O(n)
    def __init__(self, size):
        super().__init__()
        self.items = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size

    # inserting a node into a binary tree
    # Runtime complexity O(1) Space Complexity O(1)
    def insertNode(self, value):
        if (self.items is None) and (self.lastUsedIndex+1  == self.maxSize):
            return False
        self.items[self.lastUsedIndex+1] = value
        self.lastUsedIndex += 1
        return True

    # Searching a binary tree using levelOrderTraversal
    # Run time complexity O(n) & Space Complexity O(1)
    def search(self, value):
        # if binary tree exists and is not empty
        # Search for the given value 
        if (self.items is not None) and (self.lastUsedIndex > 0):
             for i in range(len(self.items)):
                 if self.items[i] == value:
                     return self.items[i]
        return None

    # Traversing a tree using preOrderTraversal
    # Run time complexity O(n) & 
    # Space Complexity O(n) --> because we are using recursion, function calls are kept on the stack
    def preOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
           
        print(self.items[index])
        self.preOrderTraversal(2*index)
        self.preOrderTraversal((2*index) + 1)
        
    # Traversing a tree using inOrderTraversal
    # Run time complexity O(n) & 
    # Space Complexity O(n) --> because we are using recursion, function calls are kept on the stack
    def inOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return

        self.inOrderTraversal(2 * index)
        print(self.items[index])
        self.inOrderTraversal((2 * index) + 1)


    # Traversing a tree using postOrderTraversal
    # Run time complexity O(n) & 
    # Space Complexity O(n) --> because we are using recursion, function calls are kept on the stack
    def postOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return

        self.postOrderTraversal(2 * index)
        self.postOrderTraversal((2 * index) + 1)
        print(self.items[index])

    # Traversing a tree using levelOrderTraversal
    # Run time complexity O(n) & Space Complexity O(1)
    def levelOrderTraversal(self, index):
        for i in range(index, self.lastUsedIndex+1):
            print(self.items[i])


    # Deleting a node in binary tree
    # Run time complexity O(n) & Space Complexity O(1)
    def deleteNode(self, value):
        if self.lastUsedIndex == 0:
            print("Binary Tree is empty")
            return False
        else:
            for i in range(1, self.lastUsedIndex+1):
                if self.items[i] == value:
                    self.items[i] = self.items[self.lastUsedIndex]
                    self.items[self.lastUsedIndex] = None
                    self.lastUsedIndex -= 1
                    print("Value Deleted")
                    return True
            print("Value was not found")
            return False

    # Deleting entire binary tree
    # Run time complexity O(1) & Space Complexity O(1)
    def deleteBinaryTree(self):
        self.items = None
        self.lastUsedIndex = 0
        self.maxSize = 0
        print("Binary Tree Deleted")
        return True



newBt = BinaryTree(10)
newBt.insertNode("Drinks")
newBt.insertNode("Hot")
newBt.insertNode("Cold")
newBt.insertNode("Tea")
newBt.insertNode("Coffee")
newBt.insertNode("Beer")
newBt.insertNode("Soda")

print("--- PreOrder Traversal ---")
newBt.preOrderTraversal(1)
print("--- End PreOrder Traversal --- \n\n")

print("--- InOrder Traversal ---")
newBt.inOrderTraversal(1)
print("--- End of InOrder Traversal --- \n\n")

print("--- PostOrder Traversal ---")
newBt.postOrderTraversal(1)
print("--- End of PostOrder Traversal --- \n\n")

print("--- LevelOrder Traversal ---")
newBt.levelOrderTraversal(1)
print("--- End of LevelOrder Traversal --- \n\n")

print("Searching for Coffee, Found --> ",newBt.search("Coffee"))
print("Searching for Scotch, Found --> ",newBt.search("Scotch"), "\n\n")

print("--- Deleting Node with Value 'Cold' ---")
print("Delete Successful? ", newBt.deleteNode("Cold"))
print("--- Printing Values after deletion ---")
newBt.levelOrderTraversal(1)
print("-------- \n\n")

# print("--- Deleting Entire BinaryTree ---")
# print("Deletion Successful? ", newBt.deleteBinaryTree())
# print("--- Printing Values after deletion ---")
# newBt.levelOrderTraversal(1)
# print("--------\n\n")