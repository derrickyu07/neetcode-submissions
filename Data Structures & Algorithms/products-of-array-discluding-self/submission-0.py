class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        temp = [1] * len(nums)
        for i in range(len(nums)-1,-1,-1):
            temp[i] = pre
            pre *= nums[i]
        post = 1
        for i in range(len(nums)):
            temp[i] *= post
            post *= nums[i]
        return temp