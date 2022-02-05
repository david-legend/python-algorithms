from heapq import *
import math

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
    n = 0
    sorted_iters = [iter(x) for x in lists]
    
    for i, l in enumerate(sorted_iters):
        n += len(lists[i])
        first_element = next(l, None)
        
        if first_element is not None:
            heappush(min_heap, (first_element, i))
   
    median = 0
    # compute index of median in sorted array
    k = math.ceil(n / 2)
    # check if length of array is even
    even = True if n % 2 == 0 else False 
    # if length of array is even increase k by 1
    k = k + 1 if even else k
    
    while k > 0:
        element, index = heappop(min_heap)
        next_array = sorted_iters[index]
        next_element = next(next_array, None)
        
        if next_element is not None:
            heappush(min_heap, (next_element, index))
        
        if k == 1 and not even:
            median = element
        elif k < 3 and even:
            median += element/2
        
        k -= 1  
    
    return  median








def main():
    print("Median from lists:: " +
        str(merge_arrays([[3, 5, 7], [0, 6], [0, 6, 28]])))
    print("Median from lists:: " +
        str(merge_arrays([[2, 6, 8], [3, 6, 7], [1, 3, 4]])))
    print("Median from lists::" +
        str(merge_arrays([[5, 8, 9], [1, 7]])))


main()