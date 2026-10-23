class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        res = [intervals[0]]
        for i in range(len(intervals)):
            temp = res[-1][1]
            if temp >= intervals[i][0]:
                res[-1][1] = max(temp,intervals[i][1])
            else:
                res.append(intervals[i])
        return res