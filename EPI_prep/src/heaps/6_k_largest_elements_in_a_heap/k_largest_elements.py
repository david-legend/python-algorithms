from heapq import *

# Time O(klogk) | Space O(k)
def k_largest_elements(data, k):
    max_heap = [(-data[0], 0)]
    result = []
    for i in range(k):
        max_element, idx = heappop(max_heap)
        left_child_idx = 2 * idx + 1

        if left_child_idx < len(data):
            heappush(max_heap, (-data[left_child_idx], left_child_idx))
        
        right_child_idx = 2 * idx + 2
        if right_child_idx < len(data):
            heappush(max_heap, (-data[right_child_idx], right_child_idx))
        
        result.append(-max_element)
    
    return result



print(k_largest_elements([561,314,401,28,156,359,271,11,3], 4)) # [561, 401, 359, 314]
