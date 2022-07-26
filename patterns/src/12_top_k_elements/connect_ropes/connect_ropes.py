from heapq import *

# Time complexity O(N*logN)
# Given ‘N’ ropes, we need O(N*logN) to insert all the ropes in the heap. 
# In each step, while processing the heap, we take out two elements 
# from the heap and insert one. 
# This means we will have a total of ‘N’ steps, having a total time complexity of O(N*logN).

# Space complexity O(N)
# The space complexity will be O(N) because we need to store all the ropes in the heap.

def minimum_cost_to_connect_ropes(rope_lengths):
    min_heap = []
    for i in range(len(rope_lengths)):
        heappush(min_heap, rope_lengths[i])

    min_cost = 0
    while len(min_heap) > 1:
        sum = heappop(min_heap) + heappop(min_heap) 
        min_cost += sum
        heappush(min_heap, sum)

    return min_cost


print("Minimum cost to connect ropes: " +
        str(minimum_cost_to_connect_ropes([1, 3, 11, 5])))
print("Minimum cost to connect ropes: " +
    str(minimum_cost_to_connect_ropes([3, 4, 5, 6])))
print("Minimum cost to connect ropes: " +
    str(minimum_cost_to_connect_ropes([1, 3, 11, 5, 2])))



