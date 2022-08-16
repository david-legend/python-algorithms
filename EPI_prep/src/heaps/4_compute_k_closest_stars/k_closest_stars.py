import heapq
import math

class Star:
    def __init__(self, x, y, z) -> None:
        self.x, self.y, self.z = x, y, z

    @property
    def distance(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def __lt__(self, other):
        return self.distance < other.distance

# Time O(nlogk) 
# Space O(k)
def compute_k_closest_stars(stars, k):
    max_heap = []

    for star in stars:
        # Add each star to the nax-heap. If the max-heap size exceeds k, 
        # remove # the naxinum elenent fron the nax-heap.
        if len(max_heap) < k:
            heapq.heappush(max_heap, (-star.distance, star))
        else:
            heapq.heappushpop(max_heap, (-star.distance, star))
    
    return [s[1] for s in heapq.nlargest(k, max_heap)]


data =  [Star(1,1,1), Star(0, 0, 1), Star(0, 1, 0), Star(2,2,2), Star(1,2,1)]

print(compute_k_closest_stars(data, 2))
print(compute_k_closest_stars(data, 3))
print(compute_k_closest_stars(data, 4))