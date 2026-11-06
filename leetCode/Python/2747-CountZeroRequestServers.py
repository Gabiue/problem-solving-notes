# 2747. Count Zero Request Servers (Medium)
# https://leetcode.com/problems/count-zero-request-servers/
# For each query q, count how many of the n servers received no request
# in the time window [q - x, q] (inclusive), using the (server_id, time) logs.

from collections import defaultdict
from typing import List

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda log: log[1])
        order = sorted(range(len(queries)), key=lambda i: queries[i])
        in_window = defaultdict(int)
        ans = [0] * len(queries)
        left = right = 0

        for i in order:
            q = queries[i]
            while right < len(logs) and logs[right][1] <= q:
                in_window[logs[right][0]] += 1
                right += 1
            while left < right and logs[left][1] < q - x:
                server = logs[left][0]
                in_window[server] -= 1
                if in_window[server] == 0:
                    del in_window[server]
                left += 1
            ans[i] = n - len(in_window)
        return ans
