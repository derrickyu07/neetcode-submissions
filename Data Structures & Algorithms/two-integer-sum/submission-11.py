class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {}
        for k,v in enumerate(nums):
            if target - v in temp:
                return [temp[target-v],k]
            temp[v] = k
