# 66. Plus One (Easy)
# https://leetcode.com/problems/plus-one/
# digits holds a big number, one digit per position (most significant first).
# Add 1 to it and return the new list of digits.

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        # add from the right: a 9 becomes 0 and carries 1 to the left
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        # every digit was 9 (e.g. 99 -> 100): the carry becomes a new digit
        return [1] + digits
