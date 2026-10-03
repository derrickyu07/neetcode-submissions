class Solution:
    def longestPalindrome(self, s: str) -> str:
        resLen = 0
        resIdx = 0
        for i in range(len(s)):
            l = i
            r= i
            while l >= 0 and r < len(s) and s[r] == s[l]:
                if resLen < r -l +1:
                    resLen = r - l+1
                    resIdx = l
                r+=1
                l-=1
            l = i
            r = i+1
            while l >= 0 and r < len(s) and s[r] == s[l]:
                if resLen < r -l +1:
                    resLen = r - l+1
                    resIdx = l
                r+=1
                l-=1
        return s[resIdx:resIdx+ resLen]