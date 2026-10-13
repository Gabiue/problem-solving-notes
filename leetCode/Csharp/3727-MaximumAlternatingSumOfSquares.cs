// 3727. Maximum Alternating Sum of Squares (Medium)
// https://leetcode.com/problems/maximum-alternating-sum-of-squares/
// Rearrange nums in any order to maximize the alternating score
// arr[0]^2 - arr[1]^2 + arr[2]^2 - arr[3]^2 + ...

public class Solution {
    public long MaxAlternatingSum(int[] nums) {
        for(int i = 0;i<nums.Length; i++)
        {
            nums[i] *= nums[i];
        }
        Array.Sort(nums);
        int minusSlots = nums.Length/2;
        long score = 0;

        for(int i = 0; i < nums.Length; i++)
        {
            if (i < minusSlots)
            {
                score -= nums[i];
            }
            else
            {
                score += nums[i];
            }
        }
        return score;
    }
}
