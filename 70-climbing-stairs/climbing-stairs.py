class Solution:
    def climbStairs(self, n: int) -> int:
        x = 0
        a = 0
        b = 1
        while x < n:
            a,b = b, a+b
            x+= 1
        return b