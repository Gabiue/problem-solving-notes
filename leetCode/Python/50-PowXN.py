# 50. Pow(x, n) (Medium)
# https://leetcode.com/problems/powx-n/
# Compute x raised to the integer power n (n can be negative or huge)
# without calling the built-in power function.

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n == 0:
            return 1.0

        half = self.myPow(x, n // 2)  # computed once, then squared
        if n % 2 == 0:
            return half * half
        return x * half * half
