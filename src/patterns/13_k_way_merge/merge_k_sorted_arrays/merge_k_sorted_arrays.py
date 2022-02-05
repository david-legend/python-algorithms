from heapq import *


# Time complexity
# Since we’ll be going through all the elements of all arrays and 
# will be removing/adding one element to the heap in each step, 
# the time complexity of the above algorithm will be O(N*logK), 
# where ‘N’ is the total number of elements in all the ‘K’ input arrays.

# Space complexity
# The space complexity will be O(K) because, at any time, 
# our min-heap will be storing one number from all the ‘K’ input arrays.
def merge_arrays(lists):
    min_heap = []
    
    sorted_iter = [iter(x) for x in lists]
    
    for i, l in enumerate(sorted_iter):
        first_element = next(l, None)
        if first_element is not None:
            heappush(min_heap, (first_element, i))
    
    result = []     
    while min_heap:
        element, index = heappop(min_heap)
        result.append(element)
        next_iter = sorted_iter[index]
        next_element = next(next_iter, None)
        
        if next_element is not None:
            heappush(min_heap, (next_element, index))
        
    return result  








def main():
    print("elements from the merged list:: " +
        str(merge_arrays([[3, 5, 7], [0, 6], [0, 6, 28]])))
    print("elements from the merged list:: " +
        str(merge_arrays([[2, 6, 8], [3, 6, 7], [1, 3, 4]])))
    print("elements from the merged list::" +
        str(merge_arrays([[5, 8, 9], [1, 7]])))


main()