class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        res = 0
        for price in prices[1:]:
            lowest = min(lowest,price)
            res = max(res,price - lowest)
        return res