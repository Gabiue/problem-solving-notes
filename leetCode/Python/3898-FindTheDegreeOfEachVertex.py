# 3898. Find the Degree of Each Vertex (Easy)
# https://leetcode.com/problems/find-the-degree-of-each-vertex/
# Given the adjacency matrix of an undirected graph, return how many
# edges touch each vertex (its degree).

class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        return [sum(row) for row in matrix]  # each 1 in row i is one edge of vertex i
