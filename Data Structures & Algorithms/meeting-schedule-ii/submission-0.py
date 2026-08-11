"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        events = []
        count = 0 
        res = 0 
        for interval in intervals:
            events.append((interval.start, 1))
            events.append((interval.end, -1))
        events.sort()
        for t, delta in events:
            count += delta
            res = max(res, count)

        return res