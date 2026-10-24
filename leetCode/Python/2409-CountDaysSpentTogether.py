# 2409. Count Days Spent Together (Easy)
# https://leetcode.com/problems/count-days-spent-together/
# Given Alice's and Bob's arrival and leave dates ("MM-DD", inclusive),
# return how many days both are in Rome at the same time.

class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def day_of_year(date: str) -> int:
            month, day = int(date[:2]), int(date[3:])
            return sum(days[:month - 1]) + day

        start = max(day_of_year(arriveAlice), day_of_year(arriveBob))
        end = min(day_of_year(leaveAlice), day_of_year(leaveBob))
        return max(0, end - start + 1)
