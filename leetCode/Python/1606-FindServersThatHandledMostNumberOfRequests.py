# 1606. Find Servers That Handled Most Number of Requests (Hard)
# https://leetcode.com/problems/find-servers-that-handled-most-number-of-requests/
# Request i goes to server i % k if free, else the next free server (wrapping
# around); dropped if all are busy. Return the servers that handled the most.

import heapq
from sortedcontainers import SortedList

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        available = SortedList(range(k))
        busy = []
        count = [0] * k
        for i in range(len(arrival)):
            start = arrival[i]
            while busy and busy[0][0] <= start:
                _, server = heapq.heappop(busy)
                available.add(server)
            if not available:
                continue
            pos = available.bisect_left(i % k)
            if pos == len(available):
                pos = 0
            server = available.pop(pos)
            count[server] += 1
            heapq.heappush(busy, (start + load[i], server))
        best = max(count)
        return [s for s in range(k) if count[s] == best]
