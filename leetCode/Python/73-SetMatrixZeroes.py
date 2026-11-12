# 73. Set Matrix Zeroes (Medium)
# https://leetcode.com/problems/set-matrix-zeroes/
# If a cell is zero, set every cell in its row and column to zero.
# Modify the matrix in place.


class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        rows_to_zero = set()
        columns_to_zero = set()

        for row in range(len(matrix)):
            for column in range(len(matrix[0])):
                if matrix[row][column] == 0:
                    rows_to_zero.add(row)
                    columns_to_zero.add(column)

        for row in range(len(matrix)):
            for column in range(len(matrix[0])):
                if row in rows_to_zero or column in columns_to_zero:
                    matrix[row][column] = 0
