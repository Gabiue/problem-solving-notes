# 3789. Minimum Cost to Acquire Required Items (Medium)
# https://leetcode.com/problems/minimum-cost-to-acquire-required-items/
# Items of type 1, type 2 or "both" (counts for both types) have their own price.
# Return the cheapest way to get at least need1 of type 1 and need2 of type 2.

class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        common = min(need1, need2)
        pair = min(costBoth, cost1 + cost2)  # one unit of each type
        only1 = min(cost1, costBoth)         # extra type 1 units
        only2 = min(cost2, costBoth)         # extra type 2 units
        return common * pair + (need1 - common) * only1 + (need2 - common) * only2
