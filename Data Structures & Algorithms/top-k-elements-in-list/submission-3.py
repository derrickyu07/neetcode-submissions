class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numDict = {}
        freq = [[] for i in range(len(nums)+1)]

        for num in nums:
            numDict[num] = numDict.get(num,0) + 1
        for i, v in numDict.items():
            freq[v].append(i)
        res = []
        for i in range(len(freq)-1,-1,-1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res