// 2333. Minimum Sum of Squared Difference (Medium)
// https://leetcode.com/problems/minimum-sum-of-squared-difference/
// Given two arrays and up to k1 + k2 single-step (+1/-1) modifications,
// minimize the sum of (nums1[i] - nums2[i])^2 over all indices.

public class Solution {
    public long MinSumSquareDiff(int[] nums1, int[] nums2, int k1, int k2) {
        long k = (long)k1 +k2;
        long [] count = new long [100001];
        int maxDiff = 0;
        for(int i = 0; i < nums1.Length; i++)
        {
            int d = Math.Abs(nums1[i] - nums2[i]);
            count[d]++;
            maxDiff = Math.Max(maxDiff,d);
        }

        //greddy
        for (int d = maxDiff; d>0 && k>0; d--)
        {
            if (count[d] <= k)
            {
                k-= count[d];
                count[d-1] +=count[d];
                count[d] = 0;
            }
            else
            {
                count [d] -= k;
                count[d-1] +=k;
                k= 0;
            }
        }
        long total = 0;
        for (int d = 1; d<= maxDiff; d++)
        {
            total += count[d] *d*d;
        }
        return total;
    }
}
