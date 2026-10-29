# 1768. Merge Strings Alternately (Easy)
# https://leetcode.com/problems/merge-strings-alternately/
# Merge two strings by taking letters alternately, starting with word1.
# Leftover letters from the longer string go at the end.

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        for k in range(max(len(word1), len(word2))):
            if k < len(word1):
                result.append(word1[k])
            if k < len(word2):
                result.append(word2[k])
        return ''.join(result)
