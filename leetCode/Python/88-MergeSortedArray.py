# 88. Merge Sorted Array (Easy)
# https://leetcode.com/problems/merge-sorted-array/
# Merge two sorted arrays into nums1, in place. nums1 has length m + n:
# the first m elements are real values, the last n are zeros to make room.

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        nums1[:] = nums1[:m] + nums2[:n]
        nums1.sort()
