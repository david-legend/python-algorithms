from heapq import *

# Time complexity O(NlogN)
# The time complexity of the above algorithm is O(N*logN), 
# where ‘N’ is the total number of jobs. 
# This is due to the sorting that we did in the beginning. 
# Also, while iterating the jobs, we might need to poll/offer jobs to the priority queue. 
# Each of these operations can take O(logN). 
# Overall our algorithm will take O(NlogN).

# Space complexity O(N)
# The space complexity of the above algorithm will be O(N), 
# which is required for sorting. Also, in the worst case, 
# we have to insert all the jobs into the priority queue (when all jobs overlap) 
# which will also take O(N) space. 
# The overall space complexity of our algorithm is O(N).
class job:
    def __init__(self, start, end, cpu_load):
        self.start = start
        self.end = end
        self.cpu_load = cpu_load

    def __lt__(self, other):
        # min heap based on job.end
        return self.end < other.end


def find_max_cpu_load(jobs):
    # sort the jobs by start time
    jobs.sort(key=lambda x: x.start)
    max_cpu_load, current_cpu_load = 0, 0
    min_heap = []

    for j in jobs:
        # remove all the jobs that have ended
        while(len(min_heap) > 0 and j.start >= min_heap[0].end):
            current_cpu_load -= min_heap[0].cpu_load
            heappop(min_heap)
        # add the current job into min_heap
        heappush(min_heap, j)
        current_cpu_load += j.cpu_load
        max_cpu_load = max(max_cpu_load, current_cpu_load)
    return max_cpu_load


print("Maximum CPU load at any time: " + str(find_max_cpu_load([job(1, 4, 3), job(2, 5, 4), job(7, 9, 6)])))
print("Maximum CPU load at any time: " + str(find_max_cpu_load([job(6, 7, 10), job(2, 4, 11), job(8, 12, 15)])))
print("Maximum CPU load at any time: " + str(find_max_cpu_load([job(1, 4, 2), job(2, 4, 1), job(3, 6, 5)])))
