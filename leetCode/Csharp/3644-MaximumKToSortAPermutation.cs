// 3644. Maximum K to Sort a Permutation (Medium)
// https://leetcode.com/problems/maximum-k-to-sort-a-permutation/
// Given a permutation of [0..n-1], you may swap nums[i] and nums[j] only if
// nums[i] AND nums[j] == k. Return the maximum k that allows sorting the array
// with any number of such swaps (0 if already sorted).

public class Solution {
    public int SortPermutation(int[] nums) {
        int result = -1; // all bits set, so the first AND keeps the value
        bool anyMisplaced = false;

        for (int i = 0; i < nums.Length; i++) {
            if (nums[i] != i) {
                result &= nums[i];
                anyMisplaced = true;
            }
        }

        return anyMisplaced ? result : 0;
    }
}
