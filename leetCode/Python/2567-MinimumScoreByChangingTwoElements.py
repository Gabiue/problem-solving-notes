# 2567. Minimum Score by Changing Two Elements (Medium)
# https://leetcode.com/problems/minimum-score-by-changing-two-elements/
# Score = max difference + min difference between any two numbers.
# Change two elements to make the score as small as possible.

class Solution:
    def minimizeSum(self, nums: list[int]) -> int:
        nums.sort()
        # low score becomes 0 by copying an existing value, so only the
        # max - min range matters: drop 2 smallest, 2 largest, or 1 of each
        return min(
            nums[-1] - nums[2],
            nums[-3] - nums[0],
            nums[-2] - nums[1],
        )
