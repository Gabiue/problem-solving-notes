# 1267. Count Servers that Communicate (Medium)
# https://leetcode.com/problems/count-servers-that-communicate/
# In a 0/1 grid, two servers communicate if they share a row or a column.
# Return how many servers communicate with at least one other server.

class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        rows = [0] * len(grid)
        cols = [0] * len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    rows[i] += 1
                    cols[j] += 1

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (rows[i] > 1 or cols[j] > 1):
                    count += 1
        return count
