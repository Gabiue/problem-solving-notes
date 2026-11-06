# 459. Repeated Substring Pattern (Easy)
# https://leetcode.com/problems/repeated-substring-pattern/
# Return True if s can be built by repeating one of its substrings
# two or more times.

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # cutting the ends of s + s breaks the two trivial copies of s;
        # if s still appears in the middle, it is made of a repeated pattern
        return s in (s + s)[1:-1]
