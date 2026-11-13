# 860. Lemonade Change (Easy)
# https://leetcode.com/problems/lemonade-change/
# Each lemonade costs $5 and customers pay with $5, $10 or $20 bills.
# Starting with no change, return true if you can give everyone correct change.

class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        five = ten = 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if five == 0:
                    return False
                five -= 1
                ten += 1
            else:  # bill == 20
                if ten >= 1 and five >= 1:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True
