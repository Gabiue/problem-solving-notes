# 1672. Richest Customer Wealth (Easy)
# https://leetcode.com/problems/richest-customer-wealth/
# Return the largest sum of account balances held by one customer.


class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        best = 0

        for i in range(len(accounts)):
            esum = 0
            for j in range(len(accounts[i])):
                esum += accounts[i][j]

            best = max(esum, best)

        return best
