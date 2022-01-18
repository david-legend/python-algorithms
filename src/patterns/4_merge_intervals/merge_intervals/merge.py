# Time Complexity
# The time complexity of the algorithm is O(N * logN), 
# where ‘N’ is the total number of intervals. 
# We are iterating the intervals only once which will take O(N), 
# in the beginning though, since we need to sort the intervals, 
# our algorithm will take O(N * logN).

# Space complexity
# The space complexity of the algorithm will be O(N) 
# as we need to return a list containing all the merged intervals. 
# We will also need O(N) space for sorting. 
# Python uses the Timsort algorithm which needs O(N) space. 
# Overall, our algorithm has a space complexity of O(N).

def merge(intervals):
    if len(intervals) < 2:
        return intervals
    
    intervals.sort(key=lambda x: x[0])
    
    merged_intervals = []
    start = intervals[0][0]
    end = intervals[0][1]
    
    for i in range(1, len(intervals)):
        interval = intervals[i]
        
        if interval[0] <= end:
            end = max(end, interval[1])
        else:
            merged_intervals.append([start, end])
            start = interval[0]
            end = interval[1]
    
    merged_intervals.append([start, end])
    
    return merged_intervals



print(merge([[1, 4], [2, 5], [7, 9]]))
print(merge([[6, 7], [2, 4], [5, 9]]))
print(merge([[1, 4], [2, 6], [3, 5]]))