from heapq import *

# Time complexity
# First, we inserted at most ‘K’ or one element from each of the ‘N’ rows, 
# which will take O(min(K, N)). Then we went through at most ‘K’ elements in the 
# matrix and remove/add one element in the heap in each step. 
# As we can’t have more than ‘N’ elements in the heap in any condition, 
# therefore, the overall time complexity of the above algorithm will be O(min(K, N) + K*logN).

# Space complexity
# The space complexity will be O(N) because, in the worst case, 
# our min-heap will be storing one number from each of the ‘N’ rows.

def find_Kth_smallest(matrix, k):
    number = -1
    min_heap = []
    sorted_iter = [iter(x) for x in matrix]

    for i in range(min(k, len(matrix))):
        next_element = next(sorted_iter[i], None)

        if next_element is not None:
            heappush(min_heap, (next_element, i))

    while min_heap and k > 0:
        number, index = heappop(min_heap)
        next_row = sorted_iter[index]
        next_element = next(next_row, None)

        if next_element is not None:
            heappush(min_heap, (next_element, index))

        k -= 1

    return number


def main():
    print("Kth smallest number is: " +
        str(find_Kth_smallest([[2, 6, 8], [3, 7, 10], [5, 8, 11]], 5)))


main()
