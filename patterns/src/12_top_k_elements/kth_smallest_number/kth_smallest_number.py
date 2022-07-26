from heapq import *

# Time complexity O(N∗logK)
# The time complexity of this algorithm is O(K*logK + (N-K)*logK), 
# which is asymptotically equal to O(N*logK)

# Space complexity O(K)
# The space complexity will be O(K) since we need to store the top ‘K’ numbers in the heap.

def find_Kth_smallest_number(nums, k):
    max_heap = []
    # put first k numbers in the max heap
    for i in range(k):
        heappush(max_heap, -nums[i])
    
    # go through the remaining numbers of the array, if the number from the array is smaller than the
    # top(biggest) number of the heap, remove the top number from heap and add the number from array
    for i in range(k, len(nums)):
        if -nums[i] > max_heap[0]:
            heappop(max_heap)
            heappush(max_heap, -nums[i])
            
    # the root of the heap has the Kth smallest number        
    return -max_heap[0]


# Solution 2
# Time Complexity - O(N+KlogN)
# Initializing the min-heap with all numbers will take O(N) 
# and extracting ‘K’ numbers will take O(KlogN). 
# Overall, the time complexity of this algorithm will be O(N+KlogN)

# Space complexity - O(N).
def find_Kth_smallest_number_2(nums, k):
    min_heap = []
    for num in nums:
        heappush(min_heap, num)
    
    kth_smallest = 0
    for _ in range(k):
        kth_smallest = heappop(min_heap)
        
    return kth_smallest
   
print("Kth smallest number is: " +
        str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 3)))

# since there are two 5s in the input array, our 3rd and 4th smallest numbers should be a '5'
print("Kth smallest number is: " +
    str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 4)))

print("Kth smallest number is: " +
    str(find_Kth_smallest_number([5, 12, 11, -1, 12], 3)))