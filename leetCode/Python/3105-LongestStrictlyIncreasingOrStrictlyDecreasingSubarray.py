# 3105. Longest Strictly Increasing or Strictly Decreasing Subarray (Easy)
# https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/
# Return the length of the longest contiguous piece of nums that is
# strictly increasing or strictly decreasing.

class Solution:
    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        best = up = down = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                up, down = up + 1, 1
            elif nums[i] < nums[i - 1]:
                up, down = 1, down + 1
            else:
                up = down = 1
            best = max(best, up, down)
        return best
