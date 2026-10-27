# 3963. Create Grid With Exactly One Path (Easy)
# https://leetcode.com/problems/create-grid-with-exactly-one-path/
# Build any m x n grid of '.' (free) and '#' (obstacle) so that there is
# exactly one path from (0, 0) to (m-1, n-1) moving only right or down.

class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        # create the real path
        grid = []

        for i in range(m):
            row = []
            for j in range(n):
                if i == 0 or j == n -1:
                    row.append('.')
                else:
                    row.append('#')
            grid.append(''.join(row))
        return grid
