def find_interval(intervals):
    if len(intervals) < 2:
        return False
    
    intervals.sort(key=lambda x: x[0])
    
    start = intervals[0][0]
    end = intervals[0][1]
    
    for i in range(1, len(intervals)):
        interval = intervals[i]
        if interval[0] <= end:
            return True
        else:
            start = interval[0]
            end = interval[1]
    
    return False


print(find_interval([[1, 4], [2, 5], [7, 9]]))
print(find_interval([[6,7], [9,12]]))