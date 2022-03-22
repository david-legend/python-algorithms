# Time complexity O(N)
# Since we are iterating through all the intervals only once, 
# the time complexity of the algorithm will be O(N), 
# where ‘N’ is the total number of intervals.

# Space complexity O(N) 
# The space complexity of the above algorithm will be O(N) 
# as we need to return a list containing all the merged intervals.

def insert(intervals, new_interval):
    merged_intervals = []
    i, start, end = 0, 0, 1
    
    while i < len(intervals) and intervals[i][end] < new_interval[start]:
        merged_intervals.append(intervals[i])
        i += 1
    
    while i < len(intervals) and intervals[i][start] < new_interval[end]:
        new_interval[start] = min(new_interval[start], intervals[i][start])
        new_interval[end] = max(new_interval[end], intervals[i][end])
        i += 1
        
    merged_intervals.append(new_interval)
    
    while i < len(intervals):
        merged_intervals.append(intervals[i])
        i += 1
        
    return merged_intervals


print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 6])))
print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 10])))
print("Intervals after inserting the new interval: " + str(insert([[2, 3], [5, 7]], [1, 4])))
