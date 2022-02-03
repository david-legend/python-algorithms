from heapq import *

# Time complexity
# The time complexity of the above algorithm is O(N + N * logK).

# Space complexity
# The space complexity will be O(N). 
# Even though we are storing only ‘K’ numbers in the heap. 
# For the frequency map, however, we need to store all the ‘N’ numbers.

def find_k_frequent_numbers(nums, k):
    top_numbers = []
    min_heap = []
    num_frequency_map = {}
    
    for num in nums:
        num_frequency_map[num] = num_frequency_map.get(num, 0) + 1
    
    for num, frequency in num_frequency_map.items():
        heappush(min_heap, (frequency, num))
        if len(min_heap) > k:
            heappop(min_heap)
    
    while len(min_heap) > 0:
        top_numbers.append(heappop(min_heap)[1])
    
    return top_numbers







print("Here are the K frequent numbers: " +
    str(find_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11], 2)))

print("Here are the K frequent numbers: " +
    str(find_k_frequent_numbers([5, 12, 11, 3, 11], 2)))



