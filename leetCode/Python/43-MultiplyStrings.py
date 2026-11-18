# 43. Multiply Strings (Medium)
# https://leetcode.com/problems/multiply-strings/
# Multiply two non-negative integers given as strings and return the
# product as a string, without converting the inputs to int directly.

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m, n = len(num1), len(num2)
        res = [0] * (m + n)  # the product has at most m + n digits

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                total = (ord(num1[i]) - 48) * (ord(num2[j]) - 48) + res[i + j + 1]
                res[i + j + 1] = total % 10
                res[i + j] += total // 10

        result = "".join(map(str, res)).lstrip("0")
        return result or "0"
