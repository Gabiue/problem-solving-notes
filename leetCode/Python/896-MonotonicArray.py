# 896. Monotonic Array (Easy)
# https://leetcode.com/problems/monotonic-array/
# Return true if nums is entirely non-decreasing or entirely non-increasing,
# false otherwise.

from itertools import pairwise

# Approach 1: compare with the sorted copies. O(n log n), 110 ms.
# return sorted(nums) == nums or sorted(nums, reverse=True) == nums

# Approach 2: check each neighbor pair once. O(n), 14 ms.
class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        return all(x <= y for x, y in pairwise(nums)) or all(x >= y for x, y in pairwise(nums))
