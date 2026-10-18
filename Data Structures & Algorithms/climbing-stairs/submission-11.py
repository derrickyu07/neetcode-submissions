class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        num1 = 1
        num2 = 1

        for i in range(n):
            temp = num1 + num2
            num1 = num2
            num2 = temp
        return num1
