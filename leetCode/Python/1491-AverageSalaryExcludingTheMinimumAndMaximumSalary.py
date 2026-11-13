# 1491. Average Salary Excluding the Minimum and Maximum Salary (Easy)
# https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/
# Given an array of unique salaries, return the average of all salaries
# excluding the minimum and maximum values.

class Solution:
    def average(self, salary: list[int]) -> float:
        salary.remove(max(salary))
        salary.remove(min(salary))
        return sum(salary) / len(salary)
