# 389. Find the Difference (Easy)
# https://leetcode.com/problems/find-the-difference/
# t is s shuffled plus one extra letter at a random position.
# Return the extra letter.

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # equal letters cancel out (a ^ a = 0), only the extra one remains
        x = 0
        for c in s + t:
            x ^= ord(c)
        return chr(x)
