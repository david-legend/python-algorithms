from heapq import *

# Time complexity
# Since we’ll be going through at most ‘K’ elements among all the arrays, 
# and we will remove/add one element in the heap in each step, 
# the time complexity of the above algorithm will be O(K*logM) 
# where ‘M’ is the total number of input arrays.

# Space complexity
# The space complexity will be O(M) because, at any time, 
# our min-heap will be storing one number from all the ‘M’ input arrays.

def find_Kth_smallest(lists, k):
    number = -1
    min_heap = []
    # Builds a list of iterators for each array in sorted-arrays 
    sorted_iters = [iter(x) for x in lists]
    
    # Puts first elenent fron each iterator in nin_heap.
    for i,l in enumerate(sorted_iters):
        first_element = next(l, None)
        if first_element is not None:
            heappush(min_heap, (first_element, i))

    while min_heap and k > 0:
        number, index = heappop(min_heap)
        next_list = sorted_iters[index]
        next_element = next(next_list, None)

        if next_element is not None:
            heappush(min_heap, (next_element, index))

        k -= 1
    return number


def main():
    print("Kth smallest number is: " +
        str(find_Kth_smallest([[2, 6, 8], [3, 6, 7], [1, 3, 4]], 5)))
    print("Kth smallest number is: " +
        str(find_Kth_smallest([[5, 8, 9], [1, 7]], 3)))


main()
