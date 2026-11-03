class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        maxTemp = 1
        minTemp = 1
        for num in nums:
            num1 = num * maxTemp
            num2 = num * minTemp
            maxTemp = max(num1, num2, num)
            minTemp = min(num1,num2, num)
            res = max(res, maxTemp)
        return res