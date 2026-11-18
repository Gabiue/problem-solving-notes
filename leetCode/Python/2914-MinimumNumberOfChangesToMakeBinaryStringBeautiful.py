# 2914. Minimum Number of Changes to Make Binary String Beautiful (Medium)
# https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/
# Change as few characters as possible so the binary string can be split
# into even-length blocks made of only 0's or only 1's.

class Solution:
    def minChanges(self, s: str) -> int:
        # any valid block splits into pairs, so each pair just needs equal chars
        return sum(s[i] != s[i + 1] for i in range(0, len(s), 2))
