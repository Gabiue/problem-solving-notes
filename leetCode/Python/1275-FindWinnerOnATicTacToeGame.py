# 1275. Find Winner on a Tic Tac Toe Game (Easy)
# https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/
# Given the moves of a 3x3 tic-tac-toe game (A plays first), return "A" or "B"
# if someone wins, "Draw" if the board is full, or "Pending" otherwise.

class Solution:
    def tictactoe(self, moves: list[list[int]]) -> str:
        rows, cols = [0] * 3, [0] * 3
        diag = anti = 0
        for i, (r, c) in enumerate(moves):
            p = 1 if i % 2 == 0 else -1  # A adds +1, B adds -1
            rows[r] += p
            cols[c] += p
            if r == c:
                diag += p
            if r + c == 2:
                anti += p
            if 3 in (abs(rows[r]), abs(cols[c]), abs(diag), abs(anti)):
                return "A" if p == 1 else "B"
        return "Draw" if len(moves) == 9 else "Pending"
