class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        else:
            x = 1
            a, b = 0, 1
            while x < n:
                a, b = b, a + b
                x +=1
            return b