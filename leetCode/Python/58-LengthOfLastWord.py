# 58. Length of Last Word (Easy)
# https://leetcode.com/problems/length-of-last-word/
# Given a string of words and spaces, return the length of the last word,
# ignoring any trailing spaces.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])
