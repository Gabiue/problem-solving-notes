# 27. Remove Element (Easy)
# https://leetcode.com/problems/remove-element/
# Remove every occurrence of val from nums in place and return k,
# the count of remaining elements. The first k slots must hold them.

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        removes = 0
        temp = 0
        while val in nums:
            nums.remove(val)
            removes += 1
        while removes > 0:
            nums.append('_')
            removes -= 1
            temp += 1

        return len(nums)-temp
