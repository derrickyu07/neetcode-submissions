class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        numSet = set()
        res = 0
        for i in range(len(s)):
            while s[i] in numSet:
                numSet.remove(s[l])
                l+=1
            numSet.add(s[i])
            res = max(res,len(numSet))
        return res
            