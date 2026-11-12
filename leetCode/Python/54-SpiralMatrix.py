# 54. Spiral Matrix (Medium)
# https://leetcode.com/problems/spiral-matrix/
# Return every element of a matrix in clockwise spiral order,
# starting from the top-left corner.


class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        result = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            for column in range(left, right + 1):
                result.append(matrix[top][column])
            top += 1

            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1

            if top <= bottom:
                for column in range(right, left - 1, -1):
                    result.append(matrix[bottom][column])
                bottom -= 1

            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1

        return result
