# 1524. Number of Sub-arrays With Odd Sum (Medium)
# https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/
# Count the subarrays whose sum is odd, modulo 1e9 + 7.
# A subarray sum is odd when its two prefix sums have different parity.

class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        even = 1  # empty prefix (sum 0) counts as even
        odd = 0
        cur = 0  # parity of the running sum: 0 = even, 1 = odd
        ans = 0
        for x in arr:
            cur = (cur + x) % 2
            if cur == 1:  # running sum is odd -> pairs with earlier even prefixes
                ans += even
                odd += 1
            else:  # running sum is even -> pairs with earlier odd prefixes
                ans += odd
                even += 1
        return ans % MOD
