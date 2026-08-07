class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temp = {}
        freq = [[] for _ in range(len(nums)+ 1)]
        for num in nums:
            temp[num] = temp.get(num,0) + 1
        for i,j in temp.items():
            freq[j].append(i)
        res = []
        for i in range(len(freq)-1,-1,-1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res

        return -1