# 1041. Robot Bounded In Circle (Medium)
# https://leetcode.com/problems/robot-bounded-in-circle/
# A robot at (0, 0) facing north repeats "G"/"L"/"R" instructions forever.
# Return true if it stays inside some circle (never drifts away).

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # N, E, S, W (clockwise)
        x = y = d = 0
        for c in instructions:
            if c == "G":
                x += dirs[d][0]
                y += dirs[d][1]
            elif c == "R":
                d = (d + 1) % 4
            else:
                d = (d + 3) % 4  # left = 3 rights
        # back home, or not facing north: repeating 4 times always returns home
        return (x, y) == (0, 0) or d != 0
