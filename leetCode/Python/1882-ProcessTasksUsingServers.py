# 1882. Process Tasks Using Servers (Medium)
# https://leetcode.com/problems/process-tasks-using-servers/
# Task j arrives at second j and goes to the free server with the smallest
# weight (tie: smallest index). Return which server handles each task.

import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        free = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(free)
        busy = []
        ans = []
        time = 0
        for j, duration in enumerate(tasks):
            time = max(time, j)
            if not free:
                time = max(time, busy[0][0])
            while busy and busy[0][0] <= time:
                _, w, i = heapq.heappop(busy)
                heapq.heappush(free, (w, i))
            w, i = heapq.heappop(free)
            ans.append(i)
            heapq.heappush(busy, (time + duration, w, i))
        return ans
