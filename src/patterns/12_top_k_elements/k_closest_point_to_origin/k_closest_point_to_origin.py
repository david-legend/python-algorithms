from heapq import *

class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.distance = self.distance_from_origin()

    # used for max-heap
    def __lt__(self, other):
        return self.distance > other.distance

    def distance_from_origin(self):
        # ignoring sqrt to calculate the distance
        return (self.x * self.x) + (self.y * self.y)

    def print_point(self):
        print("[" + str(self.x) + ", " + str(self.y) + "] ", end='')
  
 
# Time complexity is (N*logK) 
# The time complexity of this algorithm is (N*logK) 
# as we iterating all points and pushing them into the heap.

# Space complexity O(K)
# The space complexity will be O(K) because we need to store ‘K’ point in the heap.    
   
def find_closest_points(points, k):
    max_heap = []
    
    for i in range(k):
        heappush(max_heap, points[i])
    
    for i in range(k, len(points)):
        if points[i].distance < max_heap[0].distance:
            heappop(max_heap)
            heappush(max_heap, points[i])
    
    return list(max_heap)


test_1 = find_closest_points([Point(1, 3), Point(3, 4), Point(2, -1)], 2)
print("Here are the k points closest the origin: ", end='')
for point in test_1:
    point.print_point()
 
print("\n\n")
    
test_2 = find_closest_points([Point(1, 2), Point(1, 3)], 1)
print("Here are the k points closest the origin: ", end='')
for point in test_2:
    point.print_point()