// 1541. Minimum Insertions to Balance a Parentheses String (Medium)
// https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/
// Each '(' must be closed by two CONSECUTIVE ')' ("))"), coming after it.
// Return the minimum number of '(' or ')' insertions to balance the string.

public class Solution {
    public int MinInsertions(string s) {
        int open = 0;
        int ans = 0;
        int i = 0;
        while (i < s.Length)
        {
            if(s[i] == '(')
            {
                open ++;
                i++;
            }
            else
            {
                                if (i + 1 < s.Length && s[i + 1] == ')')
                {
                    i += 2;
                }
                else
                {
                    ans++;
                    i++;
                }

                if (open > 0)
                {
                    open--;
                }
                else
                {
                    ans ++;
                }
            }
        }
        return ans + 2 * open;
    }
}
