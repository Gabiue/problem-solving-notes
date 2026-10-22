// 3942. Minimum Operations to Sort a Permutation (Medium)
// https://leetcode.com/problems/minimum-operations-to-sort-a-permutation/
// Given a permutation of 0..n-1, sort it using only "reverse the whole array"
// and "rotate left by one". Return the minimum number of operations, or -1.

public class Solution {
    public int MinOperations(int[] nums) {
        int n = nums.Length;
        int best = int.MaxValue;

        int t = Array.IndexOf(nums, 0);
        if (IsCyclicSorted(nums, t)) {
            best = Math.Min(t, 2 + (n - t) % n);
        }

        int[] rev = (int[])nums.Clone();
        Array.Reverse(rev);
        int u = Array.IndexOf(rev, 0);
        if (IsCyclicSorted(rev, u)) {
            best = Math.Min(best, 1 + Math.Min(u, (n - u) % n));
        }

        return best == int.MaxValue ? -1 : best;
    }

    private bool IsCyclicSorted(int[] a, int start) {
        int n = a.Length;
        for (int i = 0; i < n; i++) {
            if (a[(start + i) % n] != i) return false;
        }
        return true;
    }
}
