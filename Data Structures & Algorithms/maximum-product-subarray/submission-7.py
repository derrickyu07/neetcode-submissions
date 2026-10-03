class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        numMax = 1
        numMin = 1
        res = nums[0]
        for num in nums:
            temp1 = numMax * num
            temp2 = numMin * num
            numMax = max(temp1,temp2, num)
            numMin = min(temp1,temp2,num)
            res = max(res,numMax)
        return res