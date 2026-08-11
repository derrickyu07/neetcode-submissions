class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        res = 0
        while l <r :
            water = min(heights[l],heights[r]) * (r-l)
            res = max(res,water)
            if heights[l] > heights[r]:
                r-=1
            else:
                l+=1
        return res