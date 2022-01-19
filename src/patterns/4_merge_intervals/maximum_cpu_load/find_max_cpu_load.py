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
def find_max_cpu_load(jobs):
    jobs.sort(key=lambda x : x[0])
    start, end, job = 0, 1, 2
    max_load = 0
    curr_load = 0
    min_heap = []
    
    for i in range(len(jobs)):
        
        j = i - 1
        while len(min_heap) > 0 and jobs[i][start] >= min_heap[0]:
            # subtract load of leaving jobs from current load 
            curr_load -= jobs[j][job]
            heappop(min_heap)
        
        # add incoming job loads to curr_load
        curr_load += jobs[i][job]
        heappush(min_heap, jobs[i][end])
        
        # the max_load is equal to the max of job 
        # ever processed at a particular point in time
        max_load = max(max_load, curr_load)

    return max_load


print("Maximum CPU load at any time: " + str(find_max_cpu_load([[1,4,3], [2,5,4], [7,9,6]]) ))
print("Maximum CPU load at any time: " + str(find_max_cpu_load([[6,7,10], [2,4,11], [8,12,15]]) ))
print("Maximum CPU load at any time: " + str(find_max_cpu_load([[1,4,2], [2,4,1], [3,6,5]]) ))