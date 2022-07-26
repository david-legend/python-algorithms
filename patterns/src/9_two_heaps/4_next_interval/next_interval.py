from heapq import *
class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def find_next_interval(intervals):
    N = len(intervals)
    start_max_heap, end_max_heap = [], []
    start = 0
    
    for i in range(N):
        heappush(start_max_heap, (-intervals[i].start, i))
        heappush(end_max_heap, (-intervals[i].end, i))
    
    result = [-1 for i in range(N)]
    for _ in range(N):
        end_time, end_idx = heappop(end_max_heap)
        if -start_max_heap[0][start] >= -end_time:
            start_time, start_idx = heappop(start_max_heap)
            
            while start_max_heap and -start_max_heap[0][start] >= -end_time:
                start_time, start_idx = heappop(start_max_heap)
            result[end_idx] = start_idx
            heappush(start_max_heap, (start_time, start_idx))
    return result



result = find_next_interval(
[Interval(2, 3), Interval(3, 4), Interval(5, 6)])
print("Next interval indices are: " + str(result))

result = find_next_interval(
[Interval(3, 4), Interval(1, 5), Interval(4, 6)])
print("Next interval indices are: " + str(result))

