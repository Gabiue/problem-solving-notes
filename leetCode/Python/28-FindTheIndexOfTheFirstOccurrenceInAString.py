# 28. Find the Index of the First Occurrence in a String (Easy)
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
# Return the index where needle first appears inside haystack,
# or -1 if it never appears.

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
