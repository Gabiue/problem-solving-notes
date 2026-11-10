# 3693. Climbing Stairs II (Medium)
# https://leetcode.com/problems/climbing-stairs-ii/
# From step i you can jump to i+1, i+2 or i+3, paying costs[j] + (j - i)^2.
# Return the minimum total cost to go from step 0 to step n.

class Solution:
    def climbStairs(self, n: int, costs: list[int]) -> int:
        dp = [0] * (n + 1)
        for j in range(1, n + 1):
            dp[j] = min(dp[j - k] + costs[j - 1] + k * k for k in range(1, min(3, j) + 1))
        return dp[n]
