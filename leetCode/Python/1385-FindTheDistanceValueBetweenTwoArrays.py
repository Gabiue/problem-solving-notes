# 1385. Find the Distance Value Between Two Arrays (Easy)
# https://leetcode.com/problems/find-the-distance-value-between-two-arrays/
# Count the elements of arr1 that are farther than d from every element
# of arr2, i.e. no arr2[j] satisfies |arr1[i] - arr2[j]| <= d.

class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        count = 0
        for i in range(len(arr1)):
            safe = True
            for j in range(len(arr2)):
                if abs(arr1[i] - arr2[j]) <= d:
                    safe = False
                    break
            if safe:
                count += 1

        return count
