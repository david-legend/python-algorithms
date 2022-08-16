from heapq import *

def compute_median(sequence):
    min_heap, max_heap = [], []
    result = []

    for x in sequence:
        if not max_heap or x < -max_heap[0]:
            heappush(max_heap, -x)
        else:
            heappush(min_heap, x)
        
        if len(max_heap) - len(min_heap) > 1:
            heappush(min_heap, -heappop(max_heap))
        elif len(min_heap) > len(max_heap):
            heappush(max_heap, -heappop(min_heap))
        
        result.append(calculate_median(max_heap, min_heap))
    
    return result


def calculate_median(max_heap, min_heap):
    if len(max_heap) == len(min_heap):
        return -max_heap[0]/2 + min_heap[0]/2

    return -max_heap[0]






print(compute_median([1,0,3,5,2,0,1]))
print(compute_median([11,10,31,52,2,7,1]))