from heapq import *

# Solution
# A brute-force approach is to concatenate these sequences into a single array and then sort it. 
# The time complexity is O(nlogn), assuming there are n elements in total.

# The brute-force approach does not use the fact that the individual sequences are sorted. 
# We can take advantage of this fact by restricting our attention to the first remaining element in each sequence. 
# Specifically, we repeatedly pick the smallest element arnongst the first element of each of the remaining part of each of the sequences.

# A min-heap is ideal for maintaining a collection of elements when we need to add arbitrary
# values and extract the smallest element. For ease of exposition, we show how to merge sorted arrays, rather than files. 
# As a concrete example, suppose there are three sorted arrays to be merged: [3,5,7], [0,6], and [0,6,28]. 
# For simplicity, we show the min-heap as containing entries from these three arrays. 
# In practice, we need additional information for each entry, namely :
# 1. the array it is from 
# 2. its index in that array.


# The min-heap is initialized to the first entry of each arcay, i.e., it is {3, 0, 0}. 
# We extract the smallest entry, 0, and add it to the output which is (0). Then we add 6 to the min-heap which is {3,0,6} now (We chose the 0 entry corresponding 
# to the third array arbitrarily, it would be perfectly acceptable to choose from the second array.) 
# Next, extract 0, and add it to the output which is (0,0); then add 6 to the min-heap which is 13,6,61. 
# Next, extract 3, and add it to the output which is (0,0,3); then add 5 to the min-heap which is {5,6,6}. 
# Next, extract 5, and add it to the output which is (0,0,3,5); 
# then add 7 to the min-heap which is 17,6,61. 
# Next, extract 6, and add it to the output which is (0,0,3,5,6); 
# assuming 5 is selected from the second array, which has no remaining elements, the min-heap is {7,6}.

# Next, extract 6, and add it to the output which is (0,0,3,5,6,6); then add 28 to the min-heap which is 17,281. 
# Next, extract, and add it to the output which is (0,0,3,5,6,6,7); the min-heap is {28}.
# Next, extract 28, and add it to the output which is (0,0,3, 5,6,6,7,28); 
# now, all elements are processed and the output stores the sorted elements.


# Time O(nlogk) | Space O(k)
# let k be the number of input sequences and n the number of elements in the sequences
# there ane no more than k elements in the min-heap. Both extract-min and insert take O(logk) time.
# space complexity is O(k) beyond the space needed to write the final result.
def merge_sorted_arrays(sorted_arrays):
    sorted_arrays_iter = [iter(array) for array in sorted_arrays]
    min_heap = []

    for idx, array in enumerate(sorted_arrays_iter):
        first_element = next(array, None)
        if first_element is not None:
            heappush(min_heap, (first_element, idx))

    result = []
    while min_heap:
        min_val, min_val_array_idx = heappop(min_heap)
        result.append(min_val)
        next_array = sorted_arrays_iter[min_val_array_idx]
        next_element = next(next_array, None)

        if next_element is not None:
            heappush(min_heap, (next_element, min_val_array_idx))
    
    return result

print(merge_sorted_arrays([[3,5,7], [0,5], [0,6,28]])) #[0, 0, 3, 5, 5, 6, 7, 28]
print(merge_sorted_arrays([[33,51,71], [0,51], [10, 16,18]])) #[0, 10, 16, 18, 33, 51, 51, 71]