# 3619. Count Islands With Total Value Divisible by K (Medium)
# https://leetcode.com/problems/count-islands-with-total-value-divisible-by-k/
# Given a grid where positive cells are land (4-directionally connected),
# sum the values of each island and count the islands whose total is divisible by k.

class Solution:
    def countIslands(self, grid: list[list[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        def afundar(i, j):
            total = grid[i][j]
            grid[i][j] = 0
            pilha = [(i, j)]
            while pilha:
                r, c = pilha.pop()
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > 0:
                        total += grid[nr][nc]
                        grid[nr][nc] = 0
                        pilha.append((nr, nc))
            return total

        ilhas = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    if afundar(i, j) % k == 0:
                        ilhas += 1
        return ilhas
