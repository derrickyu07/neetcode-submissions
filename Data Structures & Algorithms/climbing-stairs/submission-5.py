class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        num1 = 2
        num2 = 3
        for i in range(4,n):
            temp = num2
            num2 = num2 + num1
            num1 = temp
        return num1 + num2