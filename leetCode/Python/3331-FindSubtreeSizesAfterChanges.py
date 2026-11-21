# 3331. Find Subtree Sizes After Changes (Medium)
# https://leetcode.com/problems/find-subtree-sizes-after-changes/
# Each node moves under its closest ancestor with the same letter (if any).
# Return the size of every node's subtree in the resulting tree.

import sys
sys.setrecursionlimit(300000)  # tree can be a 1e5-node line

class Solution:
    def findSubtreeSizes(self, parent: list[int], s: str) -> list[int]:
        n = len(parent)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)
        size = [1] * n
        last = {}  # letter -> closest ancestor with that letter

        def dfs(node, up):
            saved = last.get(s[node])
            last[s[node]] = node
            for child in children[node]:
                dfs(child, node)
            last[s[node]] = saved
            if node:
                size[saved if saved is not None else up] += size[node]

        dfs(0, -1)
        return size
