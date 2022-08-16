import itertools
from heapq import *

# 
# Solution: 
# The brute-force approach is to put the sequence in an array, sort it, and then print it. 
# The time complexity is O(nlogn), where n is the length of the input sequence. The space complexity is o(n).

# We can do better by taking advantage of the almost-sorted property. 
# Specifically, after we have read k + 1 numbers, 
# the smallest number in that group must be smaller than all following numbers. 
# For the given example sequence =[3,-1,2,6,4,5,8], k = 2, 
# after we have read the first 3 numbers, 3, -1.,2, the smallest, -1, must be globally the smallest. 
# This is because the sequence was specified to have the property that every number is at most 2 away from its final sorted location 
# and the smallest number is at index 0 in sorted order. 
# After we read in the 4, the second smallest number must be the minimum of 3,2,4, i.e.,2.

# To solve this problem in the general setting, we need to store k + 1 numbers and want to be able to efficiently 
# extract the minimum number and add a new number. A min-heap is exactly what we need. We add the first k numbers to a min-heap. 
# Now, we add additional numbers to the min-heap and extract the minimum from the heap. 
# (When the numbers run out, we just perform the extraction.)


# Time O(nlogk) 
# Space O(k) - ignoring the space for storing the result
# n = number of elements in the sequence and k = the maximum number by which each element is sorted
def sort_approximately_sorted_array(sequence, k):
    sequence = iter(sequence)
    min_heap = []
    result = []

    for x in itertools.islice(sequence, k):
        heappush(min_heap, x)
    
    for x in sequence:
        smallest = heappushpop(min_heap, x)
        result.append(smallest)
    
    while min_heap:
        smallest = heappop(min_heap)
        result.append(smallest)
    
    return result



print(sort_approximately_sorted_array([3,-1,2,6,4,5,8], 2))
print(sort_approximately_sorted_array([-4, 0, 1, -3,], 3))