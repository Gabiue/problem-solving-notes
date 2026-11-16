# 2243. Calculate Digit Sum of a String (Easy)
# https://leetcode.com/problems/calculate-digit-sum-of-a-string/
# While len(s) > k, split s into groups of k digits, replace each group
# with the sum of its digits, and join the results. Return the final s.

class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            groups = [s[i:i + k] for i in range(0, len(s), k)]
            s = "".join(str(sum(int(d) for d in g)) for g in groups)
        return s
