// 3551. Minimum Swaps to Sort by Digit Sum (Medium)
// https://leetcode.com/problems/minimum-swaps-to-sort-by-digit-sum/
// Given distinct positive integers, sort them by digit sum (ties broken
// by the smaller value) and return the minimum number of swaps needed
// to rearrange the array into that order.

using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int MinSwaps(int[] nums) {
        int n = nums.Length;

        // 1. Target order: by digit sum, then by value
        int[] sorted = nums.OrderBy(x => DigitSum(x)).ThenBy(x => x).ToArray();

        // 2. Map each value to the index where it must end up
        var target = new Dictionary<int, int>();
        for (int i = 0; i < n; i++)
            target[sorted[i]] = i;

        // 3. Count cycles: a cycle of size k needs k - 1 swaps,
        //    so the total is n - cycles
        bool[] visited = new bool[n];
        int cycles = 0;
        for (int i = 0; i < n; i++) {
            if (visited[i]) continue;
            cycles++;

            int j = i;
            while (!visited[j]) {
                visited[j] = true;
                j = target[nums[j]];   // jump to where the number at j must go
            }
        }

        return n - cycles;
    }

    private int DigitSum(int x) {
        int sum = 0;
        while (x > 0) {
            sum += x % 10;   // last digit
            x /= 10;         // drop last digit
        }
        return sum;
    }
}
