# 1572. Matrix Diagonal Sum (Easy)
# https://leetcode.com/problems/matrix-diagonal-sum/
# Return the sum of both diagonals of a square matrix,
# counting the center only once when the matrix size is odd.


class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        total = 0
        n = len(mat)

        for i in range(n):
            total += mat[i][i]
            total += mat[i][n - 1 - i]

        if n % 2 == 1:
            total -= mat[n // 2][n // 2]

        return total
