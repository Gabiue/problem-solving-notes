# 242. Valid Anagram (Easy)
# https://leetcode.com/problems/valid-anagram/
# Return True if t uses exactly the same letters as s, the same number
# of times each, in any order.

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
