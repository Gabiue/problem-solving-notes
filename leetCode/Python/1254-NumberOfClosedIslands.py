# 1254. Number of Closed Islands (Medium)
# https://leetcode.com/problems/number-of-closed-islands/
# Given a grid of 0s (land) and 1s (water), count the islands that are
# completely surrounded by water, meaning they never touch the border.

class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def afundar(i, j):
            pilha = [(i, j)]
            grid[i][j] = 1
            while pilha:
                r, c = pilha.pop()
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 0:
                        grid[nr][nc] = 1
                        pilha.append((nr, nc))

        for i in range(m):
            for j in range(n):
                na_borda = i == 0 or i == m - 1 or j == 0 or j == n - 1
                if na_borda and grid[i][j] == 0:
                    afundar(i, j)

        ilhas = 0
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if grid[i][j] == 0:
                    ilhas += 1
                    afundar(i, j)
        return ilhas
