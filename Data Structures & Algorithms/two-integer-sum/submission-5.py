class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = {}
        for i, v in enumerate(nums):
            if target - v in numDict:
                return [numDict[target-v],i]
            numDict[v] = i
         