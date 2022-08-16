from heapq import *

# Time O(klogk) | Space O(k)
def k_largest_elements(data, k):
    min_heap = []

    for val in data:
        if len(min_heap) < k:
            heappush(min_heap, val)
        else:
            heappushpop(min_heap, val)
    
    return min_heap



# if question requires answer in descending order
def k_largest_elements_1(data, k):
    min_heap = []

    for val in data:
        if len(min_heap) < k:
            heappush(min_heap, val)
        else:
            heappushpop(min_heap, val)
    
    result, idx = [None] * k, k

    while min_heap:
        result[idx - 1] = heappop(min_heap)
        idx -= 1

    return result




print(k_largest_elements([561,314,401,28,156,359,271,11,3], 4)) # [314, 359, 401, 561]
print(k_largest_elements_1([561,314,401,28,156,359,271,11,3], 4)) # [561, 401, 359, 314]