class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res = nums[0]
        maxTemp = 1
        minTemp = 1
        for num in nums:
            temp1 = num * maxTemp
            temp2 = num * minTemp
            maxTemp = max(temp1,temp2,num)
            minTemp = min(temp1,temp2,num)
            res = max(res,maxTemp)
        return res