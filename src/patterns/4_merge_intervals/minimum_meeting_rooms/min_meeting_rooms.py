from heapq import *

def min_meeting_rooms(meetings):
    meetings.sort(key=lambda x : x[0])
    start, end = 0,1
    min_rooms = 0
    min_heap = []
    
    for i in range(len(meetings)):
        # if the min_heap > 0 and the start time 
        # of the current meeting doesn't overlap with the meeting that ends the earliest
        # then we pop that meeting 
        while (len(min_heap) > 0 and meetings[i][start] >= min_heap[0]):
            heappop(min_heap)

        # push the current meeting into the minHeap
        heappush(min_heap, meetings[i][end])
        # the min_rooms required is equal to the number of rooms 
        # required at a point in time where there is the most conflict
        min_rooms = max(min_rooms, len(min_heap))
        
    return min_rooms



print("Minimum meeting rooms required: " + str(min_meeting_rooms([[4, 5],[2, 3], [2, 4], [3, 5]]))) #Output:2
print("Minimum meeting rooms required: " + str(min_meeting_rooms([[6,7], [2,4], [8,12]]))) #Output:1
print("Minimum meeting rooms required: " + str(min_meeting_rooms([[1,4], [2,5], [7,9]]))) #Output:2
print("Minimum meeting rooms required: " + str(min_meeting_rooms([[1,4], [2,3], [3,6]])))  #Output:2
    
