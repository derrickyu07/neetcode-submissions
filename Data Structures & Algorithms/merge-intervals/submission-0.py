class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair: pair[0])
        res = [intervals[0]]
        for x,y in intervals:
            temp = res[-1][1]
            if x <= temp:
                res[-1][1] = max(y,temp)
            else:
                res.append([x,y])
        return res