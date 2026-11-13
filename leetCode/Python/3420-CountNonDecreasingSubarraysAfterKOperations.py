# 3420. Count Non-Decreasing Subarrays After K Operations (Hard)
# https://leetcode.com/problems/count-non-decreasing-subarrays-after-k-operations/
# Count the subarrays that can become non-decreasing using at most k "+1" operations.
# Cost of a subarray = sum of (running max - value) over its elements.

from collections import deque


class Solution:
    def countNonDecreasingSubarrays(self, nums: list[int], k: int) -> int:
        q = deque()  # "leaders": indices whose value is the running max, left to right
        cost = ans = 0
        r = len(nums) - 1
        for l in range(len(nums) - 1, -1, -1):
            # nums[l] enters on the left and swallows smaller leaders
            while q and nums[q[0]] <= nums[l]:
                j = q.popleft()
                nxt = q[0] if q else r + 1
                cost += (nums[l] - nums[j]) * (nxt - j)
            q.appendleft(l)
            # too expensive: drop elements from the right
            while cost > k:
                cost -= nums[q[-1]] - nums[r]
                if q[-1] == r:
                    q.pop()
                r -= 1
            ans += r - l + 1
        return ans
