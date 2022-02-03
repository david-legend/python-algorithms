from heapq import *

# Time complexity O(N∗logK)
# The time complexity of this algorithm is O(K*logK + (N-K)*logK), 
# which is asymptotically equal to O(N*logK)

# Space complexity O(K)
# The space complexity will be O(K) since we need to store the top ‘K’ numbers in the heap.
def find_k_largest_numbers(nums, k):
    min_heap = []
    
    # put first 'K' numbers in the min heap
    for i in range(k):
        heappush(min_heap, nums[i])
    
    # go through the remaining numbers of the array, if the number from the array is bigger than the
    # top(smallest) number of the min-heap, remove the top number from heap and add the number from array
    for i in range(k, len(nums)):
        if nums[i] > min_heap[0]:
            heappop(min_heap)
            heappush(min_heap, nums[i])
            
    # the heap has the top 'K' numbers, return them in a list
    return list(min_heap)





print("Here are the top K numbers: " +
    str(find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3)))

print("Here are the top K numbers: " +
    str(find_k_largest_numbers([5, 12, 11, -1, 12], 3)))