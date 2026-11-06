# 3736. Minimum Moves to Equal Array Elements III (Easy)
# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-iii/
# One move adds 1 to a single element. Return the fewest moves
# needed to make all elements of nums equal.

class Solution:
    def minMoves(self, nums: list[int]) -> int:
        # values only go up, so everyone climbs to the current maximum
        top = max(nums)
        return sum(top - x for x in nums)
