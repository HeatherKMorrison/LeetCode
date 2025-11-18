class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        else:
            x = 2
            a, b, c = 0, 1, 1
            while x < n:
                a, b, c = b, c , a + b + c
                
                x +=1
            return c