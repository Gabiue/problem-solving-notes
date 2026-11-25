# 3512. Minimum Operations to Make Array Sum Divisible by K (Easy)
# https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k/
# Each operation subtracts 1 from any element. Return the fewest
# operations needed to make the sum of nums divisible by k.

class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        return sum(nums) % k  # each -1 lowers the sum by 1, so remove exactly the remainder
