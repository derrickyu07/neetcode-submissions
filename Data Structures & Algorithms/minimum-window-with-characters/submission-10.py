class Solution:
    def minWindow(self, s: str, t: str) -> str:
        resLen = float('infinity')
        resIdx = [-1,-1]
        window = {}
        tDict = {}
        for i in range(len(t)):
            tDict[t[i]] = tDict.get(t[i],0)+1
        have = 0
        need = len(tDict)
        l=0

        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c,0)+1
            if c in tDict and tDict[c] == window[c]:
                have +=1
            while need == have:
                if resLen > r -l +1:
                    resLen = r - l + 1
                    resIdx = [l,r]
                window[s[l]]-=1
                if s[l] in tDict and window[s[l]] < tDict[s[l]]:
                    have-=1
                l+=1
        l,r = resIdx
        return s[l:r+1] if resLen != float('infinity') else ''