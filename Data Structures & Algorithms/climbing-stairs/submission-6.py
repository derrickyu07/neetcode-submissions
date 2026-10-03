class Solution:
    def climbStairs(self, n: int) -> int:
        num1 = 1
        num2 = 1
        for i in range(n):
            temp = num2
            num2 = num1 + num2
            num1 = temp
        return num1