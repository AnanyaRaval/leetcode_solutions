#https://leetcode.com/problems/meeting-rooms-ii/

from typing import List
import heapq

"""
TECHNIQUE: Nested traversal of array
PROCEDURE: 
1. Sort intervals by start time.
2. Sort intervals by end time.
3. Create a dictionary for frequency of unique meetings.
4. Run a for loop through sorted end intervals
    4.1 If the meeting is already considered, continue the loop. No processing necessary.
    4.2 Mark the meeting as considered for a room. This meetings time will not be considered again.
    4.3 Run a nested loop through sorted start intervals for each end time.
        4.3.1 If the meeting hasn't been considered before and its start interval is greater than end,
              mark this meeting as considered. 
        4.3.2 Take the previous meeting and find the next consecutive meeting.
    4.4 Once all consecutive meetings are found, increment value of room. All the meetings will take place in this room.
NOTE: We are finding all sets of meetings which can take place in 1 room sequentially.
TIME COMPLEXITY: O(n^2 + nlogn)
SPACE COMPLEXITY: O(n)
"""
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        s_intervals = list(map(tuple, sorted(intervals, key=lambda x:x[0])))
        e_intervals = list(map(tuple, sorted(intervals, key=lambda x:x[1])))
        meetings, rooms = {}, 0
        for m in s_intervals:
            if (m) in meetings:
                meetings[m] += 1
            else:
                meetings[m] = 1

        for idx in range(len(e_intervals)):
            if meetings[e_intervals[idx]] == 0:
                continue
            s, e = e_intervals[idx][0], e_intervals[idx][1]
            meetings[e_intervals[idx]] -= 1

            for j in range(len(s_intervals)):
                if meetings[s_intervals[j]] != 0 and s_intervals[j][0] >= e:
                    meetings[s_intervals[j]] -= 1
                    s, e = s_intervals[j][0], s_intervals[j][1]
            rooms += 1
        return rooms

"""
Can we reduce the nested for loop?
TECHNIQUE: 2 pointers
PROCEDURE:
    1. Extract all start times within interval and sort them.
    2. Extract all end times within interval and sort them.
    3. Initialize pointers to both start and end list.
    3. Run a while loop through sorted start times.
        3.1 If the start time is greater than end time at pointer, increment room as meeting hasn't finished.
        3.2 If the start time is less than or equal to current end time, we can re-use an existing room. 
            Increment the end pointer to find the next end time.
NOTE: We are calculating overlapping meetings to find out how many rooms are required.
TIME COMPLEXITY: O(nlogn + n)
SPACE COMPLEXITY: O(n)
"""
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        s_intervals = sorted(i[0] for i in intervals)
        e_intervals = sorted(i[1] for i in intervals)

        start, end, rooms = 0, 0, 0
        while start < len(intervals):
            if s_intervals[start] < e_intervals[end]:
                rooms += 1
            else:
                end += 1
            start += 1
        return rooms

"""
We can use another data structure - heap to store the minimum end time.
TECHNIQUE: Heap sort + traversal.
PROCEDURE:
    1. Extract all start times within interval and sort them.
    2. Extract all end times within interval and store them in a heap.
    3. Run a loop through the sorted start times.
        3.1 If start time is less than the minimum end time stored in the heap, increment number of rooms
        3.2 If start time is greater/equal to minimum end time in the heap, pop the min element from heap.
            Now the heap contains the next minimum end time.
TIME COMPLEXITY: O(nlogn)
SPACE COMPLEXITY: O(n)
"""
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        s_intervals = sorted(i[0] for i in intervals)
        e_intervals = [i[1] for i in intervals]
        heapq.heapify(e_intervals)
        rooms = 0
        for s in s_intervals:
            if s < e_intervals[0]:
                rooms += 1
            else:
                heapq.heappop(e_intervals)
        return rooms










