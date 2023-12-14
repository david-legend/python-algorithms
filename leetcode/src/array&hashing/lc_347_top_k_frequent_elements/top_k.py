from heapq import *

# Time: O(n)
# Space: O(n)
def topKFrequent(nums, k):
    num_count = {}
    freq_bucket = [[] for _ in range(len(nums) + 1)] 

    for num in nums:
        num_count[num] = num_count.get(num, 0) + 1

    for num, count in num_count.items():
        freq_bucket[count].append(num)
    
    result = []
    for i in range(len(freq_bucket)-1, 0, -1):
        for num in freq_bucket[i]:
            result.append(num)
            if len(result) == k:
                return result



# Time: O(n + n + nlog(n) + n) ----> O(n + nlog(n))
# Space: O(n)
def topKFrequent2(nums, k):
    num_freq, max_heap = {}, []
    for num in nums:
        num_freq[num] = num_freq.get(num, 0) + 1
    
    for num, count in num_freq.items():
        max_heap.append((-count, num))
    
    heapify(max_heap)
    result = []
    while max_heap and k > 0:
        _, num = heappop(max_heap)
        result.append(num)
        k -= 1
    
    return result
