# 3411. Maximum Subarray With Equal Products (Easy)
# https://leetcode.com/problems/maximum-subarray-with-equal-products/
# A subarray is "product equivalent" when prod == lcm * gcd of its elements.
# Return the length of the longest such subarray.

from math import gcd, lcm

class Solution:
    def maxLength(self, nums: list[int]) -> int:
        best = 0
        for i in range(len(nums)):
            prod, g, l = 1, 0, 1  # gcd(0, x) = x, lcm(1, x) = x
            for j in range(i, len(nums)):
                prod *= nums[j]
                g = gcd(g, nums[j])
                l = lcm(l, nums[j])
                if prod == l * g:
                    best = max(best, j - i + 1)
        return best
