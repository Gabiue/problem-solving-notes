# 27. Remove Element (Easy)
# https://leetcode.com/problems/remove-element/
# Remove every occurrence of val from nums in place and return k,
# the count of remaining elements. The first k slots must hold them.

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
