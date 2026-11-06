# 283. Move Zeroes (Easy)
# https://leetcode.com/problems/move-zeroes/
# Move every 0 in nums to the end, in-place, keeping the order
# of the non-zero elements.

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # read walks every position, write marks where the next non-zero goes
        write = 0
        for read in range(len(nums)):
            if nums[read] != 0:
                nums[write] = nums[read]
                write += 1

        for i in range(write, len(nums)):
            nums[i] = 0
