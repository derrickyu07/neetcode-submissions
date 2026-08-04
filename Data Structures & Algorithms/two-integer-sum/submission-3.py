class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {}
        for i,j in enumerate(nums):
            if target - j in temp:
                return [temp[target-j],i]
            temp[j] = i