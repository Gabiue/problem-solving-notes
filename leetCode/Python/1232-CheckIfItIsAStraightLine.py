# 1232. Check If It Is a Straight Line (Easy)
# https://leetcode.com/problems/check-if-it-is-a-straight-line/
# Given a list of [x, y] points, return True if all of them
# lie on the same straight line.

class Solution:
    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:
        (x0, y0), (x1, y1) = coordinates[0], coordinates[1]
        dx, dy = x1 - x0, y1 - y0

        for x, y in coordinates[2:]:
            # same slope: dy / dx == (y - y0) / (x - x0), cross-multiplied to avoid dividing by 0
            if dy * (x - x0) != dx * (y - y0):
                return False

        return True
