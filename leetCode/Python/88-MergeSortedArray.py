# 88. Merge Sorted Array (Easy)
# https://leetcode.com/problems/merge-sorted-array/
# Merge two sorted arrays into nums1, in place. nums1 has length m + n:
# the first m elements are real values, the last n are zeros to make room.

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        i = m - 1
        j = n - 1
        k = m + n - 1

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
