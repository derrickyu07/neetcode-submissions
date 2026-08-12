class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s =='':
            return ''
        tCount = {}
        window = {}
        res = [-1,-1]
        resLen = float('infinity')
        for c in t:
            tCount[c] = tCount.get(c,0)+1
        have =  0
        need = len(tCount)
        l= 0
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c,0) + 1
            if c in tCount and window[c] == tCount[c]:
                have+=1
            while have == need:
                if resLen > r-l+1:
                    resLen = r-l+1
                    res = [l,r]
                window[s[l]]-=1
                if s[l] in tCount and window[s[l]] < tCount[s[l]]:
                    have -=1
                l+=1
        l,r = res
        return s[l:r+1] if resLen != float('infinity') else ''