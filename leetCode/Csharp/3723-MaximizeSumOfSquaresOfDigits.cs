// 3723. Maximize Sum of Squares of Digits (Medium)
// https://leetcode.com/problems/maximize-sum-of-squares-of-digits/
// Find the num-digit integer whose digits add up to sum and whose
// sum of squared digits is maximal (largest integer on ties). Return "" if none exists.

using System.Data.Common;
using System.Text;

public class Solution {
    public string MaxSumOfSquares(int num, int sum) {
        if(sum> 9 * num) return "";

        var sb = new StringBuilder(num);
        for(int i = 0; i < num; i++)
        {
            int d = Math.Min(9,sum);
            sb.Append((char)('0' + d));
            sum -= d;
        }
        return sb.ToString();


    }
}
