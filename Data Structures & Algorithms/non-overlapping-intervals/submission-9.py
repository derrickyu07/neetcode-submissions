class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda x:x[1])
        lastEnd = intervals[0][1]
        res =0
        for i in intervals[1:]:
            if lastEnd > i[0]:
                res +=1
            else:
                lastEnd = i[1]
        return res