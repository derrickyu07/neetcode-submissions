class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        temp = set(nums)
        for i in range(len(nums)):
            if (nums[i] -1) not in temp:
                length = 1
                while (length + nums[i]) in temp:
                    length +=1
                res = max(length, res)
        return res