class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        numMax = 1
        numMin = 1
        res = nums[0]

        for num in nums:
            maxTemp = num * numMax
            minTemp = num * numMin
            numMax = max(maxTemp,minTemp,num)
            numMin = min(minTemp,maxTemp,num)
            res = max(res,numMax)
        return res