# 3360. Stone Removal Game (Easy)
# https://leetcode.com/problems/stone-removal-game/
# Alice removes 10 stones first, then each turn removes 1 fewer than the
# previous one; whoever can't make a move loses. Return true if Alice wins.

class Solution:
    def canAliceWin(self, n: int) -> bool:
        take = 10
        alice_turn = True
        while n >= take:
            n -= take
            take -= 1  # next player removes 1 fewer
            alice_turn = not alice_turn

        return not alice_turn  # whoever is on turn now can't move and loses
