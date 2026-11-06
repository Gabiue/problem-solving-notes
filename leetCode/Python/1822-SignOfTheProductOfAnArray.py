# 1822. Sign of the Product of an Array (Easy)
# https://leetcode.com/problems/sign-of-the-product-of-an-array/
# Return 1 if the product of all numbers in nums is positive,
# -1 if it is negative and 0 if it is zero.

class Solution:
    def arraySign(self, nums: list[int]) -> int:
        # no need to multiply: a zero makes it 0, otherwise only the
        # number of negatives matters (odd -> negative, even -> positive)
        if 0 in nums:
            return 0
        negatives = sum(1 for x in nums if x < 0)
        return -1 if negatives % 2 != 0 else 1
