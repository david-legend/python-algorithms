from heapq import *
import math

# Time complexity
# Since, at most, we’ll be going through all the elements of all the 
# arrays and will remove/add one element in the heap in each step, 
# the time complexity of the above algorithm will be O(N*logM) 
# where ‘N’ is the total number of elements in all the ‘M’ input arrays.

# Space complexity
# The space complexity will be O(M) because, 
# at any time, our min-heap will be store one number from all the ‘M’ input array'

def find_smallest_range(lists):
    min_heap = []
    sorted_iter = [iter(x) for x in lists]
    current_max = -math.inf
    range_start, range_end = 0, math.inf

    for i, l in enumerate(sorted_iter):
        first_element = next(l, None)
        if first_element is not None:
            current_max = max(current_max, first_element)
            heappush(min_heap, (first_element, i))

    while len(min_heap) == len(lists):
        number, index = heappop(min_heap)
        if range_end - range_start > current_max - number:
            range_start, range_end = number, current_max
        
        next_arr = sorted_iter[index]
        next_element = next(next_arr, None)
        if next_element is not None:
            current_max = max(current_max, next_element)
            heappush(min_heap, (next_element, index))

    print(current_max)
    return [range_start, range_end]


def main():
    print("Smallest range is: " +
        str(find_smallest_range([[1, 5, 8], [4, 12], [7, 8, 10]])))
    print("Smallest range is: " +
        str(find_smallest_range([[1, 9], [4, 12], [7, 10, 16]])))

main()

