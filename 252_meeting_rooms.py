#https://leetcode.com/problems/meeting-rooms/description/

from typing import List

"""
TECHNIQUE: Sort + Comparison with Linear Scan.
ALGORITHM:
    1. Sort intervals by end time.
    2. Run a loop over the sorted intervals
        2.1 Start from index 1
        2.2 If end of current interval is less than start of previous interval, it is an overlapping meeting. Break early and return False.
    3. After the loop, return True as the loop did not find any overlapping meetings.

TIME COMPLEXITY: O(nlogn)
SPACE COMPLEXITY: O(1)
"""
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        s_intervals = sorted(intervals, key=lambda x: x[1])
        for idx in range(1, len(s_intervals)):
            if s_intervals[idx][0] < s_intervals[idx-1][1]:
                return False
        return True

"""
TECHNIQUE: Sort + Comparison with Linear Scan.
ALGORITHM: Instead of finding an overlapping meeting, determine if all meetings take place sequentially.
    1.  Sort intervals by end time.
    2. Run a loop over the sorted intervals
        2.1 Start from index 1
        2.2 Store values: If previous interval ends before current interval starts, store True. This will imply that the current and previous meeting are sequential.
    3. Is all values are True, return True. This implies all metings are sequential and a person can attend all meetings.

TIME COMPLEXITY: O(nlogn)
SPACE COMPLEXITY: O(n)
"""
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        s_intervals = sorted(intervals, key=lambda x:x[1])
        is_serial = [s_intervals[idx-1][1] <= s_intervals[idx][0] for idx in range(1, len(s_intervals))]
        return all(is_serial)