from heapq import *

# The brute-force approach is to sort the array, without taking advantage of the k-increasing- decreasing property. 
# Sorting algorithms run in time O(n log n), where n is the length of the array.

# If k is significantly smaller than n we can do better. 
# For example , if k = 2, the input array consists of two subarrays, one increasing, the other decreasing. 
# Reversing the second subarray yields two sorted arrays, and the result is their merge. 
# It is fairly easy to merge two sorted arrays in O(n ) time.
# Generalizing, we could first reverse the order of each of the decreasing subarrays. 
# For an example with this input [57, 131, 493, 221, 294, 339, 418, 452, 190, 442]
# we would decompose A into five sorted arrays [57, 131, 493], [221], [294, 339, 418, 452], [190] and [442]



# Time O(nlogk) | Space O(k)
def sort_increasing_decreasing_array(A):
    sorted_subarrays = []
    INCREASING, DECREASING = range(2)
    subarray_type, start_idx = INCREASING, 0

    # Time O(n)
    for i in range(1, len(A) + 1):
        if (i == len(A) or 
            (A[i - 1] < A[i] and subarray_type == DECREASING) or
            (A[i-1] >= A[i] and subarray_type == INCREASING)):

            if subarray_type == INCREASING:
                sorted_subarrays.append(A[start_idx : i])
            else:
                sorted_subarrays.append(A[i-1 : start_idx - 1 : -1])
            
            start_idx = i
            subarray_type = DECREASING if subarray_type == INCREASING else INCREASING
    
    # Time O(nlogk)
    return merge_sorted_arrays(sorted_subarrays)


def merge_sorted_arrays(sorted_arrays):
    sorted_iters = [iter(x) for x in sorted_arrays]
    min_heap = []

    for idx, sorted_array in enumerate(sorted_iters):
        first_element = next(sorted_array, None)
        if first_element is not None:
            heappush(min_heap, (first_element, idx))
    
    result = []
    while min_heap:
        min_val, min_val_idx = heappop(min_heap)
        result.append(min_val)
        next_array = sorted_iters[min_val_idx]
        next_element = next(next_array, None)

        if next_element is not None:
            heappush(min_heap, (next_element, min_val_idx))
    
    return result


print(sort_increasing_decreasing_array([57, 131, 493, 221, 294, 339, 418, 452, 190, 442])) #[57, 131, 190, 221, 294, 339, 418, 442, 452, 493]