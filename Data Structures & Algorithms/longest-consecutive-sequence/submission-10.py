class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        nums.sort()
        temp = set(nums)
        for num in nums:
            if num -1 not in temp:
                length = 1
                while num + length in temp:
                    length += 1
                res =max(res,length)
        return res
        