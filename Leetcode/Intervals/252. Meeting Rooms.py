from typing import List

"""
Definition of Interval:
"""
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda item: item.start)

        for i in range(len(intervals)-1):
            if intervals[i].end > intervals[i+1].start:
                return False
        
        return True