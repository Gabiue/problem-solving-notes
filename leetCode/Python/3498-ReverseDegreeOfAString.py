# 3498. Reverse Degree of a String (Easy)
# https://leetcode.com/problems/reverse-degree-of-a-string/
# Sum, over every character, its reversed-alphabet position ('a' = 26 ... 'z' = 1)
# times its 1-indexed position in the string.

class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        for i, c in enumerate(s, start=1):  # i = 1-indexed position in the string
            total += (26 - (ord(c) - ord('a'))) * i  # 'a' -> 26, 'z' -> 1
        return total
