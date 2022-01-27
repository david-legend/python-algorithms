from heapq import *

# Time complexity
# The time complexity of the insertNum() will be O(logN) 
# due to the insertion in the heap. 
# The time complexity of the findMedian() will be O(1) 
# as we can find the median from the top elements of the heaps.

# Space complexity
# The space complexity will be O(N) because, 
# as at any time, we will be storing all the numbers.
class MedianOfAStream:
    max_heap = []
    min_heap = []
    def insert_num(self, num):
        if not self.max_heap or -self.max_heap[0] >= num:
            heappush(self.max_heap, -num)
        else:
            heappush(self.min_heap, num)

        if len(self.max_heap) > len(self.min_heap) + 1:
            heappush(self.min_heap, -heappop(self.max_heap))
        elif len(self.max_heap) < len(self.min_heap):
            heappush(self.max_heap, -heappop(self.min_heap))
            
    def find_median(self):
        if len(self.max_heap) == len(self.min_heap):
            return -self.max_heap[0] / 2.0 + self.min_heap[0] / 2.0
        
        return -self.max_heap[0] / 1.0



medianOfAStream = MedianOfAStream()
medianOfAStream.insert_num(3)
medianOfAStream.insert_num(1)
print("The median is: " + str(medianOfAStream.find_median()))
medianOfAStream.insert_num(5)
print("The median is: " + str(medianOfAStream.find_median()))
medianOfAStream.insert_num(4)
print("The median is: " + str(medianOfAStream.find_median()))
