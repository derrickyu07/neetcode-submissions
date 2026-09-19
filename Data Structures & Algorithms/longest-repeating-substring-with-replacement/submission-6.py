class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxFreq = 0
        res = 0 
        sDict = {}
        l =0

        for i in range(len(s)):
            sDict[s[i]] = sDict.get(s[i],0)+1
            maxFreq = max(maxFreq,sDict[s[i]])

            while i - l -maxFreq + 1 > k:
                sDict[s[l]] -=1
                l+=1
            
            res = max(res, i-l+1)
        return res