// 3886. Sum of Sortable Integers (Hard)
// https://leetcode.com/problems/sum-of-sortable-integers/
// For each divisor k of n, split nums into blocks of length k and cyclically
// rotate each block independently. If the whole array can end up sorted,
// k is sortable. Return the sum of all sortable k.

public class Solution {
    public int SortableIntegers(int[] nums) {
        int n = nums.Length;
        int sum = 0;

        for (int k = 1; k <= n; k++) {
            if (n % k == 0 && IsSortable(nums, k)) sum += k;
        }

        return sum;
    }

    // A block can be rotated into sorted order iff, read as a circle,
    // it goes down at most once. The whole array is sorted iff each block
    // is, and every block's min is >= the previous block's max.
    private bool IsSortable(int[] nums, int k) {
        int prevMax = int.MinValue;

        for (int start = 0; start < nums.Length; start += k) {
            int end = start + k - 1;
            int descents = 0;
            int min = nums[start];
            int max = nums[start];

            for (int j = start; j < end; j++) {
                if (nums[j] > nums[j + 1]) descents++;
                min = Math.Min(min, nums[j + 1]);
                max = Math.Max(max, nums[j + 1]);
            }
            if (nums[end] > nums[start]) descents++; // wrap-around pair

            if (descents > 1) return false;
            if (min < prevMax) return false;
            prevMax = max;
        }

        return true;
    }
}
