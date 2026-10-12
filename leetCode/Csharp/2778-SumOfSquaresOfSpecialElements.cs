// 2778. Sum of Squares of Special Elements (Easy)
// https://leetcode.com/problems/sum-of-squares-of-special-elements/
// Given a 1-indexed array nums of length n, an element nums[i] is special
// if i divides n (n % i == 0). Return the sum of the squares of all special elements.

public class Solution {
    public int SumOfSquares(int[] nums) {
        int n = nums.Length;

        int sum = 0;

        for(int i = 1 ; i<= n; i++)
        {
            if(n%i == 0)
            {
                sum += nums[i-1] * nums[i-1];
            }
        }

    return sum;
    }
}
