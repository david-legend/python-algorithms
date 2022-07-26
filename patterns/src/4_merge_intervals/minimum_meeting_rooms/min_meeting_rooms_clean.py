from heapq import *

class Meeting:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        # min heap based on meeting.end
        return self.end < other.end


# Time complexity O(NlogN)
# The time complexity of the above algorithm is O(N*logN), 
# where ‘N’ is the total number of meetings. 
# This is due to the sorting that we did in the beginning. 
# Also, while iterating the meetings we might need to poll/offer meeting to the priority queue.
# Each of these operations can take O(logN). 
# Overall our algorithm will take O(NlogN).

# Space complexity
# The space complexity of the above algorithm will be O(N) which is required for sorting. 
# Also, in the worst case scenario, 
# we’ll have to insert all the meetings into the Min Heap (when all meetings overlap) 
# which will also take O(N) space. 
# The overall space complexity of our algorithm is O(N).
def min_meeting_rooms(meetings):
    # sort the meetings by start time
    meetings.sort(key=lambda x: x.start)
    minRooms = 0
    minHeap = []
    
    for meeting in meetings:
        # remove all the meetings that have ended
        while(len(minHeap) > 0 and meeting.start >= minHeap[0].end):
            heappop(minHeap)
        # add the current meeting into min_heap
        heappush(minHeap, meeting)
        # all active meetings are in the min_heap, so we need rooms for all of them.
        minRooms = max(minRooms, len(minHeap))
    return minRooms


print("Minimum meeting rooms required: " + str(min_meeting_rooms(
[Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)])))
print("Minimum meeting rooms required: " +
    str(min_meeting_rooms([Meeting(1, 4), Meeting(2, 5), Meeting(7, 9)])))
print("Minimum meeting rooms required: " +
    str(min_meeting_rooms([Meeting(6, 7), Meeting(2, 4), Meeting(8, 12)])))
print("Minimum meeting rooms required: " +
    str(min_meeting_rooms([Meeting(1, 4), Meeting(2, 3), Meeting(3, 6)])))
print("Minimum meeting rooms required: " + str(min_meeting_rooms(
[Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)])))