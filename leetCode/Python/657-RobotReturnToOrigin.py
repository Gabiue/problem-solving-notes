# 657. Robot Return to Origin (Easy)
# https://leetcode.com/problems/robot-return-to-origin/
# A robot starts at (0, 0) and follows moves made of 'U', 'D', 'L', 'R'.
# Return true if it ends back at the origin.

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R')
