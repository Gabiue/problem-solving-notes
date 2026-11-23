# 1352. Product of the Last K Numbers (Medium)
# https://leetcode.com/problems/product-of-the-last-k-numbers/
# Design a class that receives a stream of integers (add) and
# returns the product of the last k numbers added (getProduct).

class ProductOfNumbers:

    def __init__(self):
        self.prefix = [1]  # prefix[i] = product of the last i numbers since the latest 0

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix = [1]  # a 0 kills every product that includes it
        else:
            self.prefix.append(self.prefix[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.prefix):
            return 0  # the last k numbers reach back past a 0
        return self.prefix[-1] // self.prefix[-1 - k]
