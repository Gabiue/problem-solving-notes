# 2124. Check if All A's Appears Before All B's (Easy)
# https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/
# Given a string of only 'a' and 'b', return true if every 'a'
# comes before every 'b' (no 'b' is followed by an 'a').

class Solution:
    def checkString(self, s: str) -> bool:
        if s.rfind('a') > s.find('b') and s.find('b') != -1:
            return False  # last 'a' comes after the first 'b'

        return True
