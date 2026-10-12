// 2897. Apply Operations on Array to Maximize Sum of Squares (Hard)
// https://leetcode.com/problems/apply-operations-on-array-to-maximize-sum-of-squares/
// Any number of times, pick two indices and replace them with their AND and OR.
// Then choose k elements and return the maximum sum of their squares, modulo 1e9 + 7.

public class Solution {
    public int MaxSum(IList<int> nums, int k) {
        const long MOD = 1_000_000_007;
        int [] count = new int[31];


        foreach(int num in nums)
        {
            for (int b = 0; b<31; b++)
            {
                if(((num>>b)& 1) == 1)
                {
                    count[b]++;
                }
            }
        }

        long sum = 0;

        for(int i = 0; i<k ; i++)
        {
            long x = 0;
            for(int b = 0; b <31 ; b++)
            {
                if (count[b] > 0)
                {
                    x |= 1L << b;
                    count[b]--;
                }
            }
            sum = (sum + x *x)%MOD;
        }

        return (int)sum;
    }
}
