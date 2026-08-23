class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        sSet = set()
        res = 0
        for r in range(len(s)):
            while s[r] in sSet:
                sSet.remove(s[l])
                l+=1
            sSet.add(s[r])
            res = max(res,len(sSet))
        return res
        