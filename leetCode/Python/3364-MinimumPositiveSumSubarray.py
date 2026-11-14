# 3364. Minimum Positive Sum Subarray (Easy)
# https://leetcode.com/problems/minimum-positive-sum-subarray/
# Find the minimum sum of a subarray whose length is between l and r
# (inclusive) and whose sum is greater than 0. Return -1 if none exists.
# Brute force: check every subarray (n <= 100 makes O(n^2) fine).

class Solution:
    def minimumSumSubarray(self, nums: list[int], l: int, r: int) -> int:
        n = len(nums)
        best = -1
        for i in range(n):
            s = 0
            for j in range(i, n):
                s += nums[j]
                size = j - i + 1
                if size > r:
                    break
                if size >= l and s > 0:
                    best = s if best == -1 else min(best, s)
        return best
