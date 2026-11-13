# 1523. Count Odd Numbers in an Interval Range (Easy)
# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/
# Given two non-negative integers low and high, return the count of
# odd numbers between low and high (inclusive).

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        count = 0
        for i in range(low, high + 1):
            if i % 2 != 0:
                count += 1
        return count
