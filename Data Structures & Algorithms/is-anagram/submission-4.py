class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
             return False
        temp1 = {}
        temp2 = {}
        i = 0
        while (len(s) > i):
        
            temp1[s[i]] = temp1.get(s[i],0) + 1
            temp2[t[i]] = temp2.get(t[i],0) + 1
            i +=1
        

        return temp1 == temp2