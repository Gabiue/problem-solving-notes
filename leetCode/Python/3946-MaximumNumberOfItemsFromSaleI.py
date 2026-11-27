# 3946. Maximum Number of Items From Sale I (Medium)
# https://leetcode.com/problems/maximum-number-of-items-from-sale-i/
# Buy item copies within budget; buying item i once also gives a free copy of
# every other item whose factor is divisible by factor_i. Maximize total copies.

class Solution:
    def maximumSaleItems(self, items: list[list[int]], budget: int) -> int:
        MAXF = max(f for f, _ in items)
        cnt = [0] * (MAXF + 1)
        for f, _ in items:
            cnt[f] += 1

        # dp[b] = most copies obtainable spending at most b, using the items seen so far
        dp = [0] * (budget + 1)
        for f, price in items:
            free = sum(cnt[m] for m in range(f, MAXF + 1, f)) - 1  # other items whose factor f divides
            first = 1 + free  # what the first copy of this item is worth
            new = dp[:]
            best = [-1] * (budget + 1)  # best[b] = value at budget b with this item bought at least once
            for b in range(price, budget + 1):
                best[b] = dp[b - price] + first  # buy the first copy now
                if best[b - price] >= 0:
                    best[b] = max(best[b], best[b - price] + 1)  # or one more extra copy
                new[b] = max(new[b], best[b])
            dp = new
        return dp[budget]
