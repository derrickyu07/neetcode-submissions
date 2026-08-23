class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        sDict = {}
        maxFreq = 0
        l = 0
        res = 0
        for r in range(len(s)):
            sDict[s[r]] = sDict.get(s[r],0)+ 1
            maxFreq = max(maxFreq, sDict[s[r]])

            while r-l+1-maxFreq > k:
                sDict[s[l]]-=1
                l+=1
            res = max(res,r-l+1)
        return res