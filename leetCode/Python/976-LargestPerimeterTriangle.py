# 976. Largest Perimeter Triangle (Easy)
# https://leetcode.com/problems/largest-perimeter-triangle/
# Pick three lengths from nums that form a triangle with non-zero area
# and return the largest possible perimeter, or 0 if none exists.

class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        nums.sort()

        for i in range(len(nums) - 1, 1, -1):
            if nums[i] < nums[i - 1] + nums[i - 2]:
                return nums[i] + nums[i - 1] + nums[i - 2]

        return 0
