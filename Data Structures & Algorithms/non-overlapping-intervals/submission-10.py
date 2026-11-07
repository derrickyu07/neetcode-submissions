class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[1])
        res = 0 
        bestEnd = intervals[0][1]
        for i in intervals[1:]:
            if bestEnd > i[0]:
                res +=1
            else:
                bestEnd = i[1]
        return res
