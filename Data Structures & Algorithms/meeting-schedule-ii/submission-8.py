"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        time = []
        
        for i in intervals:
            time.append([1,i.start])
            time.append([-1,i.end])
        res = count = 0
        time.sort(key = lambda x: (x[1],x[0]))

        for t in time:
            count += t[0]
            res = max(res, count)
        return res