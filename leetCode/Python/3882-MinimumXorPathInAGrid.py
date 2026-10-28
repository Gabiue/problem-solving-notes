# 3882. Minimum XOR Path in a Grid (Medium)
# https://leetcode.com/problems/minimum-xor-path-in-a-grid/
# Move from (0, 0) to (m-1, n-1) going only right or down. The cost of a
# path is the XOR of all its cells. Return the smallest possible cost.

class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # dp[i][j] = every XOR value that can arrive at cell (i, j)
        dp = [[set() for _ in range(n)] for _ in range(m)]
        dp[0][0].add(grid[0][0])

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                v = grid[i][j]
                if i > 0:
                    for x in dp[i - 1][j]:
                        dp[i][j].add(x ^ v)
                if j > 0:
                    for x in dp[i][j - 1]:
                        dp[i][j].add(x ^ v)
        return min(dp[m - 1][n - 1])
