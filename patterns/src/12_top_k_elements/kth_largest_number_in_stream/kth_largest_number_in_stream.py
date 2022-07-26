from heapq import *

# Time complexity
# The time complexity of the add() function will be O(logK) 
# since we are inserting the new number in the heap.

# Space complexity
# The space complexity will be O(K) for storing numbers in the heap.

class KthLargestNumberInStream:
    
    min_heap = []
    
    def __init__(self, nums, k):
        self.k = k
        for num in nums:
            self.add(num)
            
    def add(self, num):
        heappush(self.min_heap, num)
        
        if len(self.min_heap) > self.k:
            heappop(self.min_heap)

        return self.min_heap[0]
    

kthLargestNumber = KthLargestNumberInStream([3, 1, 5, 12, 2, 11], 4)
print("4th largest number is: " + str(kthLargestNumber.add(6)))
print("4th largest number is: " + str(kthLargestNumber.add(13)))
print("4th largest number is: " + str(kthLargestNumber.add(4)))
print("4th largest number is: " + str(kthLargestNumber.add(7)))
