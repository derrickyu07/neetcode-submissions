class Solution:
    def isValid(self, s: str) -> bool:
        sDict = {
            "}":"{",
            ")":"(",
            "]":"["
        }
        stack = []
        for c in s:
            if c in sDict:
                if stack and stack[-1] == sDict[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack