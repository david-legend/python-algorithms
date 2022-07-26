from heapq import *
import heapq

# Time complexity
# The time complexity of our algorithm is O(N*K) where ‘N’ is the total number of elements 
# in the input array and ‘K’ is the size of the sliding window. 
# This is due to the fact that we are going through all the ‘N’ numbers and, 
# while doing so, we are doing two things:

# Inserting/removing numbers from heaps of size ‘K’. This will take O(logK)
# Removing the element going out of the sliding window. This will take O(K) 
# as we will be searching this element in an array of size ‘K’ (i.e., a heap).

# Space complexity 
# Ignoring the space needed for the output array, the space complexity will be O(K) because, 
# at any time, we will be storing all the numbers within the sliding window.

class SlidingWindowMedian:
    def __init__(self):
        self.max_heap, self.min_heap = [], []
        
    def find_sliding_window_median(self, nums, k):
        result = [0.0 for x in range(len(nums) - k + 1)]
        for i in range(0, len(nums)):
            if not self.max_heap or nums[i] <= -self.max_heap[0]:
                heappush(self.max_heap, -nums[i])
            else:
                heappush(self.min_heap, nums[i])

            self.rebalance_heaps()

            if i - k + 1 >= 0:  # if we have at least 'k' elements in the sliding window
                # add the median to the the result array
                if len(self.max_heap) == len(self.min_heap):
                    # we have even number of elements, take the average of middle two elements
                    result[i - k + 1] = -self.max_heap[0] / 2.0 + self.min_heap[0] / 2.0
                else:  # because max-heap will have one more element than the min-heap
                    result[i - k + 1] = -self.max_heap[0] / 1.0

                # remove the element going out of the sliding window
                elementToBeRemoved = nums[i - k + 1]
                if elementToBeRemoved <= -self.max_heap[0]:
                    self.remove(self.max_heap, -elementToBeRemoved)
                else:
                    self.remove(self.min_heap, elementToBeRemoved)

                self.rebalance_heaps()

        return result

    def rebalance_heaps(self):
        if len(self.max_heap) > len(self.min_heap) + 1:
            heappush(self.min_heap, -heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heappush(self.max_heap, -heappop(self.min_heap))

    def remove(self, heap, val):
        ind = heap.index(val)  # find the element
        # move the element to the end and delete it
        heap[ind] = heap[-1]
        del heap[-1]
        # we can use heapify to readjust the elements but that would be O(N),
        # instead, we will adjust only one element which will O(logN)
        if ind < len(heap):
            heapq._siftup(heap, ind)
            heapq._siftdown(heap, 0, ind)
            
            
slidingWindowMedian = SlidingWindowMedian()
result = slidingWindowMedian.find_sliding_window_median(
[1, 2, -1, 3, 5], 2)
print("Sliding window medians are: " + str(result))

slidingWindowMedian = SlidingWindowMedian()
result = slidingWindowMedian.find_sliding_window_median(
[1, 2, -1, 3, 5], 3)
print("Sliding window medians are: " + str(result))


