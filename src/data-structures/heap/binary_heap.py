# assign HEAP.MAX for a maxHeap
# if nothing is assigned, then heap is automatically MIN

class Heap:
    MIN = "min"
    MAX = "max"
    # Time Complexity --> O(1)
    # Space Complexity --> O(n)
    def __init__(self, size, heapType = MIN):
        super().__init__()
        self.items = (size+1) * [None]
        self.heapSize = 0
        self.maxSize = size + 1
        self.heapType = heapType

    # Time Complexity --> O(1)
    # Space Complexity --> O(1)
    def peek(self):
        if self.heapSize == 0:
            return 
        else:
            return self.items[1]

    # Time Complexity --> O(1)
    # Space Complexity --> O(1)
    def size(self):
        if self.items is None:
            print("Heap doesn't exist")
            return None
        else:
            return self.heapSize

    # Time Complexity --> O(n)
    # Space Complexity --> O(1)
    def levelOrderTraversal(self):
        if self.items is None:
            print("Heap doesn't exist")
        else:
            for i in range(1, self.heapSize+1):
                print(self.items[i])

    def swap(self, index, parentIndex):
        temp = self.items[index]
        self.items[index] = self.items[parentIndex]
        self.items[parentIndex] = temp

    def heapifyInsert(self, index):
        parentIndex = int(index/2)
        if index <= 1:
            return
        
        if self.heapType == self.MIN:
            if self.items[index] < self.items[parentIndex]:
                self.swap(index, parentIndex)
        else:
            if self.items[index] > self.items[parentIndex]:
                self.swap(index, parentIndex)

        self.heapifyInsert(parentIndex) 


    def insertNode(self, nodeValue):
        if self.heapSize + 1 == self.maxSize:
            print("Heap is Full")
            return
        self.items[self.heapSize + 1] = nodeValue
        self.heapSize += 1
        self.heapifyInsert(self.heapSize)

    def heapifyExtract(self, index):
        leftIndex = index * 2
        rightIndex = index * 2 + 1
        swapChild = 0

        if self.heapSize < leftIndex:
            return
        elif self.heapSize == leftIndex:
            if self.heapType == self.MIN:
                if self.items[index] > self.items[leftIndex]:
                    self.swap(index, leftIndex)
                return
            else:
                if self.items[index] < self.items[leftIndex]:
                    self.swap(index, leftIndex)
                return
        else:
            if self.heapType == self.MIN:
                if self.items[leftIndex] < self.items[rightIndex]:
                    swapChild = leftIndex
                else:
                    swapChild = rightIndex
                if self.items[index] > self.items[swapChild]:
                    self.swap(index, swapChild)
            else:
                if self.items[leftIndex] > self.items[rightIndex]:
                    swapChild = leftIndex
                else:
                    swapChild = rightIndex
                if self.items[index] < self.items[swapChild]:
                    self.swap(index, swapChild)
        self.heapifyExtract(swapChild)


    def extractNode(self):
        if self.heapSize == 0:
            return
        else:
            # extract first node from tree
            extractedNode = self.items[1]
            # replace first node with last node 
            self.items[1] = self.items[self.heapSize]
            # set last node's position to None
            self.items[self.heapSize] = None
            # reduce size of heap
            self.heapSize -= 1
            # execute heapifyExtract to shuffle everything into the right place
            self.heapifyExtract( 1)
            # return the extracted node
            return extractedNode

    def deleteEntireBP(self):
        self.items = None

maxHeap = Heap(10, Heap.MIN)

maxHeap.insertNode(5)
maxHeap.insertNode(1)
# print("Extracted: ", maxHeap.extractNode())
print("--- Level Order Traversal After Insert---")
maxHeap.levelOrderTraversal()
print("\n\n")

# maxHeap.insertNode(18)
# maxHeap.insertNode(11)
# maxHeap.insertNode(19)
# maxHeap.insertNode(12)
# maxHeap.insertNode(20)
# maxHeap.insertNode(14)
# maxHeap.insertNode(48)

# print("--- Level Order Traversal After Insert---")
# maxHeap.levelOrderTraversal()
# print("\n\n")

# print("--- Extracting Node from heap ---")
# print("Extracted: ", maxHeap.extractNode())
# print("\n")
# print("--- Level Order Traversal After Extracting Node---")
# maxHeap.levelOrderTraversal()
# print("\n\n")