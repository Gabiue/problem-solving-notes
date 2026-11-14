# 3364. Minimum Positive Sum Subarray (Easy)
# https://leetcode.com/problems/minimum-positive-sum-subarray/
# Find the minimum sum of a subarray whose length is between l and r
# (inclusive) and whose sum is greater than 0. Return -1 if none exists.
# O(n log n): prefix sums + a SortedList window with binary search.

from sortedcontainers import SortedList


class Solution:
    def minimumSumSubarray(self, nums: list[int], l: int, r: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        best = -1
        window = SortedList()
        for j in range(1, n + 1):
            if j - l >= 0:
                window.add(prefix[j - l])
            if j - r - 1 >= 0:
                window.remove(prefix[j - r - 1])

            pos = window.bisect_left(prefix[j])
            if pos > 0:
                s = prefix[j] - window[pos - 1]
                best = s if best == -1 else min(best, s)
        return best
